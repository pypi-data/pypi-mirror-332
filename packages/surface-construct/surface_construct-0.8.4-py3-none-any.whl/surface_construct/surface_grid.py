"""
TODO：设置某些原子（序号、类型）不进行采样，作图的时候使用最大值填充？
TODO: 双结合位点情况。表面位点采样[(x1, y1, z1), (x2, y2, z2)]。一般化双格点采样，可以找到相对应的 (COM, bondlen, theta, phi)
      不同的键长，对应不同的双格点，
TODO: 构效关系建立。将不同的位点向量合并，然后进行性能分布的关联，投影到二维平面（PCA）。
"""
import itertools
import pickle

import ase
import matplotlib.tri as mtri
import networkx as nx
import numpy as np
from ase.data import covalent_radii, vdw_radii, chemical_symbols
from ase.geometry import find_mic
from ase.neighborlist import natural_cutoffs, primitive_neighbor_list
from ase.visualize import view
from matplotlib import pyplot as plt
from scipy.interpolate import griddata
from scipy.sparse import coo_matrix
from scipy.spatial import cKDTree
from scipy.spatial.distance import euclidean
from sklearn.decomposition import PCA
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel, WhiteKernel
from sklearn.preprocessing import StandardScaler

from surface_construct.sampling import InitialSampling, addition_samples
from surface_construct.utils import get_calc_info, get_distances, get_graph_core, wrap_grid, \
    filter_index_label, rattle, iso_surface, extended_points
from surface_construct.weight_functions import vb_weight


class GridGenerator:
    def __init__(self, atoms,
                 rads=0.76,
                 rsub=None,
                 subtype=None,
                 interval=0.1,
                 scale=None,
                 rattle_eps=0
                 ):
        """
        :param atoms: 基底结构 ase.Atoms
        :param rads: 吸附原子的半径, 默认是 C 的共价半径
        :param rsub: 基底的原子半径
            type: str, 'covalent_radii' or 'vdw_radii'
            type: list or tuple or numpy.array, [r1, r2, ... rN], N=len(atoms)
        :param subtype: 基底的类型，slab, cluster, bulk (porous material)
        :param interval:
        :param scale: scale factor of rsub and rads. For covalent_radii, the default is 1.1, otherwise it is 1.0

        TODO: 使用 s3dlib cloudsurf 构造格点，代替 marching cube. 已经验证了，太慢
        TODO: 使用周期性的 KDTree 代替当前的
        """
        self._index_type_dict = None
        self._grid_index_type = None
        self._site_type_dict = None
        self._grid_site_type = None
        self._grid_faces = None
        self._grid_graph = None
        self.atoms = atoms
        self._grid = None
        self.atoms_num_type = sorted(set(atoms.numbers))
        self.interval = interval
        self._Lga = None  # bool 矩阵，grid 与 atom 之间成键与否
        self.rattle_eps = rattle_eps

        if subtype is None:
            npbc = sum(atoms.pbc)
            if npbc == 0:
                self.subtype = 'cluster'
            elif npbc == 2:
                if atoms.pbc[-1]:
                    raise "Error: Slab should be in xy direction!"
                self.subtype = 'slab'
            elif npbc == 3:
                self.subtype = 'bulk'
            else:
                raise NotImplementedError("Subtype not implemented yet!")

        elif subtype.lower() in ['slab', 'bulk', 'cluster']:
            self.subtype = subtype.lower()
        else:
            raise NotImplementedError('Only slab, cluster, bulk and slab are implemented.')
        self._generator = getattr(self, self.subtype+'_grid')

        if type(rsub) in (list, tuple, np.ndarray):
            assert len(rsub) == len(atoms)
            self.rsub = rsub
        elif type(rsub) == dict:
            self.rsub = [rsub.get(n) or rsub.get(chemical_symbols(n)) for n in atoms.numbers]
        elif type(rsub) == str or rsub is None:
            if rsub == 'covalent_radii' or rsub == 'natural_cutoff' or rsub is None:
                self.rsub = natural_cutoffs(atoms)
                if scale is None:
                    scale = 1.1
            elif rsub == 'vdw_radii':
                self.rsub = [vdw_radii[n] for n in atoms.numbers]
        else:
            raise ValueError("rsub must be 'covalent_radii', 'natural_cutoff' or 'vdw_radii' or a list.")

        if scale is None:
            scale = 1.0
        self.scale = scale
        self.rsub = np.asarray(self.rsub) * scale
        self.rads = rads * scale

    def cluster_grid(self):
        atoms = self.atoms
        if np.all(atoms.pbc):
            atoms.center()
        interval = self.interval
        pos = atoms.positions
        # 找到团簇格点的边界
        posx, posy, posz = pos[:,0], pos[:,1], pos[:,2]
        xmin = (posx - self.rsub).min() - interval * 2 - self.rads
        xmax = (posx + self.rsub).max() + interval * 2 + self.rads
        ymin = (posy - self.rsub).min() - interval * 2 - self.rads
        ymax = (posy + self.rsub).max() + interval * 2 + self.rads
        zmin = (posz - self.rsub).min() - interval * 2 - self.rads
        zmax = (posz + self.rsub).max() + interval * 2 + self.rads
        xarray = np.arange(xmin, xmax, interval)
        yarray = np.arange(ymin, ymax, interval)
        zarray = np.arange(zmin, zmax, interval)
        Nx,Ny,Nz = map(len, [xarray, yarray, zarray])
        # 格点生成
        grid_x, grid_y, grid_z = np.meshgrid(xarray, yarray, zarray, indexing='ij')
        xyz = np.asarray([grid_x.ravel(), grid_y.ravel(), grid_z.ravel()]).T
        xyz = rattle(xyz, stdev=self.interval/3)
        grid_tree = cKDTree(xyz, copy_data=True)

        dist_max = coo_matrix((1,Nx*Ny*Nz))
        atoms_num_type = set(atoms.numbers)
        # 对于不同的原子类型取不同的半径
        for num_type in atoms_num_type:
            pos = atoms.positions[atoms.numbers == num_type]
            atoms_tree = cKDTree(pos, copy_data=True)
            max_distance = self.rads + self.rsub[atoms.numbers == num_type][0]
            sdm = atoms_tree.sparse_distance_matrix(grid_tree, max_distance=max_distance)
            # 保证没有格点的坐标跟grid 完全重合，如果有的话，需要标识出来，赋予它们另外的值，保证在后面识别中不为0。
            sdm0 = atoms_tree.sparse_distance_matrix(grid_tree, max_distance=0)
            for k in sdm0.keys():
                sdm[k] = 1
            dist_max = sdm.tocoo().nanmax(axis=0).maximum(dist_max)
        dist_max = dist_max.transpose().toarray().reshape((Nx, Ny, Nz))
        points, faces, normals = iso_surface([grid_x, grid_y, grid_z], dist_array=dist_max, level=0)
        self._grid = points
        self._grid_faces = faces

    def slab_grid(self):
        atoms = self.atoms
        pos = atoms.positions
        interval = self.interval
        posz = pos[:,2]
        zmax = (posz + np.asarray(self.rsub)).max() + self.rads + interval * 2
        zmin = (posz.max() + posz.min())/2  # 从层中心开始
        lenx, leny, lenz = atoms.cell.lengths()
        Nx, Ny = np.asarray(np.around([lenx/self.interval ,leny/self.interval]), dtype=int)
        Nz = int(np.around((zmax-zmin)/self.interval))
        fx_list = np.linspace(0,1,Nx, endpoint=False)
        fy_list = np.linspace(0,1,Ny, endpoint=False)
        fz_list = np.linspace(zmin/lenz,zmax/lenz,Nz, endpoint=False)
        fgrid_x, fgrid_y, fgrid_z = np.meshgrid(fx_list, fy_list, fz_list, indexing='ij')
        fxyz = np.asarray([fgrid_x.ravel(), fgrid_y.ravel(), fgrid_z.ravel()]).T
        xyz = atoms.cell.cartesian_positions(fxyz)
        if self.rattle_eps > 0:
            xyz = rattle(xyz, stdev=self.interval*self.rattle_eps)
            fxyz = atoms.cell.scaled_positions(xyz)  # 对于 rattle 后的xyz数据，得到fxyz
            fgrid_x = fxyz[:,0].reshape((Nx, Ny, Nz))
            fgrid_y = fxyz[:,1].reshape((Nx, Ny, Nz))
            fgrid_z = fxyz[:,2].reshape((Nx, Ny, Nz))
        grid_tree = cKDTree(xyz, copy_data=True)

        # 对atoms 在 xy 方向超胞. Adapt from ase.geometry.geometry.general_find_mic
        ranges = [np.arange(-1 * p, p + 1) for p in atoms.pbc[:2]]
        hkls = np.concatenate([np.array(list(itertools.product(*ranges))),
                               np.zeros([9, 1], dtype=int)], axis=1)
        vrvecs = hkls @ atoms.cell
        super_pos = np.concatenate(atoms.positions + vrvecs[:,None], axis=0)
        super_num = np.concatenate([atoms.numbers] * 9)
        rsub = np.concatenate([self.rsub] * 9)

        dist_max = coo_matrix((1,Nx*Ny*Nz))
        atoms_num_type = set(atoms.numbers)
        # 对于不同的原子类型取不同的半径
        for num_type in atoms_num_type:
            pos = super_pos[super_num == num_type]
            atoms_tree = cKDTree(pos, copy_data=True)
            max_distance = self.rads + rsub[super_num == num_type][0]
            sdm = atoms_tree.sparse_distance_matrix(grid_tree, max_distance=max_distance)
            # 保证没有格点的坐标跟grid 完全重合，如果有的话，需要标识出来，赋予它们另外的值，保证在后面识别中不为0。
            sdm0 = atoms_tree.sparse_distance_matrix(grid_tree, max_distance=0)
            for k in sdm0.keys():
                sdm[k] = 1
            dist_max = sdm.tocoo().nanmax(axis=0).maximum(dist_max)
        dist_max = dist_max.transpose().toarray().reshape((Nx, Ny, Nz))
        fpoints, faces, normals = iso_surface([fgrid_x, fgrid_y, fgrid_z], dist_array=dist_max, level=0)
        points = atoms.cell.cartesian_positions(fpoints)
        self._grid = points
        self._grid_faces = faces

    def bulk_grid(self):
        atoms = self.atoms
        interval = self.interval
        Nx, Ny, Nz = np.asarray(np.around(atoms.cell.lengths()/interval), dtype=int)
        fx_list = np.linspace(0,1,Nx, endpoint=False)
        fy_list = np.linspace(0,1,Ny, endpoint=False)
        fz_list = np.linspace(0,1,Nz, endpoint=False)
        fgrid_x, fgrid_y, fgrid_z = np.meshgrid(fx_list, fy_list, fz_list, indexing='ij')
        fxyz = np.asarray([fgrid_x.ravel(), fgrid_y.ravel(), fgrid_z.ravel()]).T
        xyz = atoms.cell.cartesian_positions(fxyz)
        if self.rattle_eps > 0:
            xyz = rattle(xyz, interval * self.rattle_eps)
        grid_tree = cKDTree(xyz, copy_data=True)
        # 对atoms 在 xyz 方向超胞. Adapt from ase.geometry.geometry.general_find_mic
        ranges = [np.arange(-1 * p, p + 1) for p in atoms.pbc]
        hkls = np.array(list(itertools.product(*ranges)))
        vrvecs = hkls @ atoms.cell
        super_pos = np.concatenate(atoms.positions + vrvecs[:, None], axis=0)
        super_num = np.concatenate([atoms.numbers] * len(vrvecs))
        rsub = np.concatenate([self.rsub] * len(vrvecs))
        dist_max = coo_matrix((1, Nx * Ny * Nz))
        atoms_num_type = set(atoms.numbers)
        # 对于不同的原子类型取不同的半径
        for num_type in atoms_num_type:
            pos = super_pos[super_num == num_type]
            atoms_tree = cKDTree(pos, copy_data=True)
            max_distance = self.rads + rsub[super_num == num_type][0]
            sdm = atoms_tree.sparse_distance_matrix(grid_tree, max_distance=max_distance)
            # 保证没有格点的坐标跟grid 完全重合，如果有的话，需要标识出来，赋予它们另外的值，保证在后面识别中不为0。
            sdm0 = atoms_tree.sparse_distance_matrix(grid_tree, max_distance=0)
            for k in sdm0.keys():
                sdm[k] = 1
            dist_max = sdm.tocoo().nanmax(axis=0).maximum(dist_max)
        dist_max = dist_max.transpose().toarray()
        # 反转，距离大于 max_distance 的保留，其他的去掉
        points = xyz[dist_max[:,0]==0,:]
        self._grid = points

    @property
    def grid(self):
        if self._grid is None:
            self._generator()

        return self._grid

    def view(self, tag=None):
        if len(self.grid) > 10000:
            print("Too much grid number, it will be very slow.")
        atoms = ase.Atoms(symbols=['X'] * len(self.grid), positions=self.grid)
        view(self.atoms + atoms)


class SurfaceGrid:

    def __init__(self, atoms,
                 interval=0.1,
                 vlen=10,
                 rads=None,
                 ads_num=None,
                 subtype=None,
                 rsub='natural_cutoff',
                 rscale=None,
                 lpca=True,
                 rcutoff=10.0,
                 ):
        """

        :param atoms: ase.Atoms
        :param interval: grid interval
        :param vlen: vector length for each atom type
        :param rads: radius for adsorbate, default is covalent radius of carbon
        :param ads_num: atom number of adsorbate, default is 6 (carbon)
        :param subtype: subtype: 基底的类型，slab, cluster, bulk (porous material)
        :param rsub: 基底的原子半径
            type: str, 'covalent_radii' or 'vdw_radii'
            type: list or tuple or numpy.array, [r1, r2, ... rN], N=len(atoms)
        :param rscale:  scale factor of rsub and rads. For covalent_radii, the default is 1.1, otherwise it is 1.0
        :param lpca: 是否对 vector 进行 PCA 降维，默认 True
        :param rcutoff: 求 vector 时的截断半径，默认 10. A.
        """
        self._unique_vip_id = None
        self._grid_tree = None
        self._vip_id = None
        self._gridgen = None
        self._vectorize_func = None
        self._unit_vector = None
        self._vector_interval = None
        self._index_type_dict = None
        self._grid_index_type = None
        self._site_type_dict = None
        self._grid_site_type = None
        self._grid_faces = None
        self._grid_graph = None
        self._pca = None
        self._raw_vector = None
        self._reduced_vector = None
        self._vector_dim = None
        self._sample_vector = []  # 用于作图 和 GPR
        self._clusters = None  # 仅用于作图
        self._Dga = None  # grid_atoms 距离矩阵

        self.atoms = atoms
        self.subtype = subtype
        num_set = set(self.atoms.numbers)
        num_list = list(self.atoms.numbers)
        self.species = sorted([(num, num_list.count(num)) for num in num_set], key=lambda x: x[0])

        self.rcutoff = rcutoff

        if type(rsub) in (list, tuple, np.ndarray):
            assert len(rsub) == len(atoms)
            self.rsub = rsub
        elif type(rsub) == dict:
            self.rsub = [rsub.get(n) or rsub.get(chemical_symbols(n)) for n in atoms.numbers]
        elif type(rsub) == str:
            if rsub == 'covalent_radii' or rsub == 'natural_cutoff':
                self.rsub = natural_cutoffs(atoms)
                if rscale is None:
                    rscale = 1.1
            elif rsub == 'vdw_radii':
                self.rsub = [vdw_radii[n] for n in atoms.numbers]
        else:
            raise ValueError("rsub must be 'covalent_radii', 'natural_cutoff' or 'vdw_radii' or a list.")
        if rscale is None:
            rscale = 1.0
        self.scale = rscale
        self.rsub = np.asarray(self.rsub) * rscale
        if rads is None:
            rads = self.rsub[ads_num or 6]
        self.rads = rads * rscale

        self.interval = interval
        self.vlen = vlen
        self.points = None  # 格点 xyz 坐标
        self.vector = None
        self.lpca = lpca

        self.sample_idx = None  # 采样点的 idx
        self.sample_points = None
        self.sample_property = {}
        self.grid_property = {}
        self.grid_property_sigma = {}
        self.iter = 0  # 记录进行了多少次的迭代

        self.calc_info = {}
        if atoms.calc is not None:
            self.calc_info = get_calc_info(atoms.calc)

    def initialize(self):
        # 格点化
        self.gridize()
        # 格点向量化
        self.vectorize()

    def gridize(self, **kwargs):
        """
        格点化。
        这种方法仅仅适用于无孔的材料，表面为z方向，且方向向上。
        * gridxy: [X, Y] 2D meshgrid
        * surface_index: 表面原子的序号
        :return:
        """
        subtype = kwargs.get('subtype', self.subtype)
        if subtype is None:
            subtype = 'slab' # default is slab
        self.subtype = subtype
        #rsub = [self.rsub[atomnum] for atomnum in self.atoms.numbers]
        gridgen = GridGenerator(self.atoms,
                                interval=self.interval, subtype=subtype, rads=self.rads, rsub=self.rsub)
        self.points = gridgen.grid
        self._gridgen = gridgen

    def _get_grid_tree(self, extend=False):
        if self.subtype == 'cluster' and extend:
            print("Cluster system does not need extend!")
            extend = False
        if self._grid_tree is not None:
            l_extend = len(self.points) != self._grid_tree.n
            if l_extend != extend:  # need recalculate
                self._grid_tree = None
        if self._grid_tree is None:
            if extend:
                ncell = [1, 1, 1]
                if self.subtype == 'slab':
                    ncell = [1, 1, 0]
                grid = extended_points(self.points, ncell=ncell, cell=self.atoms.cell)
            else:
                grid = self.points
            self._grid_tree = cKDTree(grid)
        return self._grid_tree

    @property
    def grid_graph(self):
        if self._grid_graph is None:
            ngrid = len(self.points)
            cutoff = self.interval * 2
            dlist, ilist = self._get_grid_tree(extend=True).query(self.points, k=7, distance_upper_bound=cutoff)  # 最近邻的原子最多为6, 包含自身则为7
            ilist = ilist % ngrid  # 折叠格点的序号
            pairs = [(ii[0], i, d) for ii, dd in zip(ilist, dlist) for i, d in zip(ii[1:], self.interval / dd[1:])]
            graph = nx.Graph()
            graph.add_weighted_edges_from(pairs)
            self._grid_graph = graph
        return self._grid_graph

    def _calc_Dga(self):
        # TODO: 使用 scipy.sparse matrix, 比如 csc_matrix
        if self.points is None:
            self.gridize()
        if self.subtype == 'slab':
            pbc = [True, True, False]
        elif self.subtype == 'cluster':
            pbc = [False, False, False]
        else:
            pbc = self.atoms.pbc
        _, Dga = get_distances(self.points, self.atoms.positions, cutoff=self.rcutoff, pbc=pbc,
                               use_ase=False, cell=self.atoms.cell)
        self._Dga = Dga

    @property
    def _Dga11(self):
        # 由于 self._calc_Dga 可能超胞了，这里需要对其进行折叠，形成 1 （格点） 对 1 （原子） 的距离矩阵。
        ng,na = len(self.points), len(self.atoms)
        if self._Dga.shape == (ng,na):
            Dga11 = self._Dga
        else:
            # 折叠之后取最小值
            Dga11 = self._Dga.reshape(ng,-1,na).min(axis=1)  # 注意顺序，测试出来的
        return Dga11

    @property
    def _Lga(self):
        """
        格点与原子的连接性。
        TODO: 使用 scipy.sparse matrix, 比如 csc_matrix
        :return:
        """
        #_, Dga = get_distances(self.points, self.atoms.positions, use_ase=True, cell=self.atoms.cell,
        #                       pbc=self.atoms.pbc)
        if self._Dga is None:
            self._calc_Dga()
        return self._Dga11 - (self.rsub + self.rads + self.interval*2) < 0  # 格点与原子的连接性。如果距离小于半径之和，则为不连接

    def get_grid_site_type(self, site_dict=None):
        """
        根据第一近邻原子类型返回格点所对应的类型
        :param site_dict: 格点的类型字典
            example: {0:(atom_num1, atom_num1, atom_num2), ..., 'next_idx':int}
        :return: site label for each grid, site_dict
        """
        if self._grid_site_type is not None:
            return self._grid_site_type, self._site_type_dict
        if site_dict is None:
            site_dict = {'next_idx': 0}
        reverse_site_dict = {v:k for k,v in site_dict.items() if type(k) == int}
        atoms_num = self.atoms.numbers
        grid_label, index_dict = self.get_grid_index_type()
        new_site_label = np.array(grid_label)
        for k,v in index_dict.items():
            num_v = tuple(sorted([atoms_num[i] for i in v]))
            if num_v not in reverse_site_dict:
                reverse_site_dict[num_v] = site_dict['next_idx']
                site_dict[site_dict['next_idx']] = num_v
                site_dict['next_idx'] += 1
            # 改变 site_label 为新的 label
            new_site_label[new_site_label==k] = reverse_site_dict[num_v]

        self._grid_site_type = new_site_label
        self._site_type_dict = site_dict
        return self._grid_site_type, self._site_type_dict

    def get_grid_index_type(self):
        """
        根据第一近邻原子序号返回格点所对应的类型
        :return: atom index label for each grid, index_dict
            index_dict: 格点的类型字典
                example: {0:(atom_idx1, atom_idx2,...)}
        """

        if self._grid_index_type is not None:
            return self._grid_index_type, self._index_type_dict
        index_label = list(set(tuple(map(int,i)) for i in self._Lga))  # 以原子类型区分，不同格点的类别集合
        index_dict = {i:tuple(np.argwhere(v).flatten()) for i,v in enumerate(index_label)}
        index_dict_reverse = {v:i for i,v in enumerate(index_label)}
        grid_label = [index_dict_reverse[tuple(i)] for i in self._Lga]
        grid_label, index_dict = filter_index_label(grid_label, index_dict)
        self._grid_index_type = grid_label
        self._index_type_dict = index_dict
        return self._grid_index_type, self._index_type_dict

    @property
    def vip_id(self):
        """
        所有表面的特殊位点，根据格点网络的质心得到
        :return:
        """
        if self._vip_id is None:
            grid_index_type, index_type_dict = self.get_grid_index_type()
            vip_points = []
            for idx in index_type_dict:
                grid_idx = np.argwhere(np.array(grid_index_type) == idx).flatten()
                graph = self.grid_graph.subgraph(grid_idx)
                lc = nx.is_connected(graph)
                if not lc:  # 如果不联通，需要重新计算 graph
                    wrapped_grid = wrap_grid(self.points[grid_idx], self.atoms.cell)
                    # 构建cKDtree
                    cutoff = self.interval * 2
                    tree = cKDTree(wrapped_grid)
                    dlist, ilist = tree.query(wrapped_grid, k=7, distance_upper_bound=cutoff)  # 最近邻的原子最多为6, 包含自身则为7
                    pairs = [(grid_idx[ii[0]], grid_idx[i], d) for ii, dd in zip(ilist, dlist)
                             for i, d in zip(ii[1:], self.interval / dd[1:]) if d > 0 ]
                    graph = nx.Graph()
                    graph.add_nodes_from(grid_idx)
                    graph.add_weighted_edges_from(pairs)

                if not nx.is_connected(graph):
                    largest_cc = max(nx.connected_components(graph), key=len)
                    graph = graph.subgraph(largest_cc)
                core_graph = get_graph_core(graph, gmin=10)
                #vip = np.mean(wrap_grid([self.grid[c] for c in nx.barycenter(core_graph)],self.atoms.cell), axis=0)
                vip = np.mean([self.points[c] for c in nx.barycenter(core_graph)], axis=0)
                vip_points.append(vip)
            vip_points = np.array(vip_points)
            vip_points_idx = self.get_near_index_from_xyz(vip_points)
            # 过滤掉一些空间距离和向量距离过近的点，d < 0.5 A
            pnl_vip = primitive_neighbor_list(quantities='ijd',
                                              positions=vip_points, cell=self.atoms.cell,
                                              cutoff=0.5, pbc=self.atoms.pbc)
            pairs_vip = [(vip_points_idx[i],vip_points_idx[j],d) for i,j,d in zip(*pnl_vip)]
            # 生成 graph，然后对每个连接的子图的 node 进行判断，标准 1. 配位数最高
            G_vip = nx.Graph()
            G_vip.add_weighted_edges_from(pairs_vip)
            exclude_idx = []
            for subg in nx.connected_components(G_vip):
                subg_list = list(subg)
                CN_list = [len(index_type_dict[grid_index_type[i]]) for i in subg_list]
                max_CN = max(CN_list)
                ex_idx =[i for i in subg_list if i!=subg_list[CN_list.index(max_CN)]]
                exclude_idx += ex_idx
            self._vip_id = [i for i in vip_points_idx if i not in exclude_idx]
        return self._vip_id

    @property
    def unique_vip_id(self):
        # 靠近中心 (0.5, 0.5, 0.5) 的非等价 vip 位点。等价的判断标准，相同的 site_type
        if self._unique_vip_id is None:
            vip_id = np.array(self.vip_id)
            grid_site_type, site_type_dict = self.get_grid_site_type()
            vip_site_type = grid_site_type[vip_id]
            center = self.atoms.cell.cartesian_positions([[0.5,0.5,0.5]])
            uid = []
            for itype in site_type_dict.keys():
                isite = vip_id[vip_site_type==itype]
                if len(isite)>0:
                    ipos = self.points[isite]
                    _, dist = get_distances(center, ipos, cell=self.atoms.cell, use_ase=True, pbc=self.atoms.pbc)
                    csite = isite[dist.argmin()]
                    uid.append(csite)
            self._unique_vip_id = uid
        return self._unique_vip_id


    def grid_NN_array(self, grid_idx):
        """
        返回表面格点最近邻原子和次紧邻原子的向量，以此方式求格点的 reference 向量。效果比较好。
        :param grid_idx:
        :return:
        """

        if self._Dga is None:
            self._calc_Dga()
        order = np.argsort(self._Dga[grid_idx])
        p1, p2 = self.atoms.positions[order[0:2]]
        v, _ = find_mic(p2-p1, cell=self.atoms.cell, pbc=self.atoms.pbc)
        return v

    def view_grid(self, tag=None):
        if len(self.points) > 10000:
            print("Too much grid number, it will be very slow.")

        if tag == 'site':
            tag, _ = self.get_grid_site_type()
        elif tag == 'index':
            tag, _ = self.get_grid_index_type()
        atoms = ase.Atoms(symbols=['X'] * len(self.points), positions=self.points, tags=tag)
        view(self.atoms + atoms)

    @property
    def grid_energy(self):
        if 'energy' in self.grid_property:
            return self.grid_property['energy']
        else:
            return None

    def vectorize(self, Dga=None, return_vector=False, wf=vb_weight, pca=None, pca_ratio=0.90, **kwargs):
        """
        TODO: 使用 DScribe 来进行向量化，并进行测试。如何测试？测试什么内容？
        TODO: 产生 cluster_mesh, 生成 cluster_mesh_id 与 point_id 之间的正反向 dict
        使用 distance matrix 来进行向量化
        使用衰减函数对 vector 加权重。备选函数：S型，指数型（键价），1/sqrt，1/x，线性。倾向使用指数型，键价理论支持。 1/x，或者 1/sqrt，衰减更慢。
        这种方法类似于多点地位方法（Multilateration），因而暂时称其为 Multilateration vectorization.
        :param pca_ratio:
        :param pca:
        :param wf:
        :param Dga: grid-atoms distance matrix
        :param return_vector: 是否返回 vector 向量
        """
        if Dga is None:
            if self._Dga is None:
                self._calc_Dga()
            Dga = self._Dga
        if pca is None:
            pca = self.lpca
        elif pca:
            self.lpca = True

        Natoms = Dga.shape[1] / len(self.atoms)  # Dga is multiple of atoms
        assert Natoms == int(Natoms)  # Natoms should be int
        numbers = np.concatenate([self.atoms.numbers]*int(Natoms))  # multiply atoms.number
        vector = []
        for atomnum, atomcount in self.species:
            grid_dist = Dga[:, numbers == atomnum]
            # 排序，返回排序后的序号
            index_array = grid_dist.argsort(axis=-1)
            grid_dist = np.take_along_axis(grid_dist, index_array, axis=-1)
            # grid_dist_array = np.take_along_axis(grid_dist_array, index_array, axis=-1)
            # 设定距离向量长度
            vlen = self.vlen
            r0 = self.rads + self.rsub[atomnum]
            v = grid_dist[:, :vlen]
            kwargs.update({'r0': r0})
            # v_w = np.concatenate([wf(v, **kwargs), np.zeros((v.shape[0], self.vlen-vlen))], axis=1)
            v_w = wf(v, **kwargs)
            vector.append(v_w)
        vector = np.concatenate(vector, axis=1)
        self._raw_vector = vector
        if not pca:  # 用于 debug
            self._vector_dim = vector.shape[1]
            self._vectorize_func = lambda x: wf(x, **kwargs)
            if return_vector:
                return vector
            else:
                self.vector = vector
                return
        # PCA 降维
        if return_vector:
            assert self._pca is not None
            reduced_vector = self._pca.transform(vector)
            return reduced_vector
        else:
            dim_max = int(3 * len(self.species))
            pca = PCA(n_components=dim_max, whiten=False)
            pca.fit(vector)
            dim = 2
            for i in range(2, dim_max):  # 最小维度为 2
                explained_variance_ratio = sum(pca.explained_variance_ratio_[:i])
                if explained_variance_ratio > pca_ratio:
                    dim = i
                    break
            self._pca = PCA(n_components=dim, whiten=False)
            self._pca.fit(vector)
            reduced_vector = self._pca.transform(vector)
            self.vector = reduced_vector
            self._vector_dim = self.vector.shape[1]
            self._vectorize_func = lambda x: self._pca.transform(wf(x, **kwargs))

    @property
    def vector_interval(self):
        """
        计算实空间和向量空间的距离转化系数。随机取十个点，求平均值。
        :return:
        """
        if self._vector_interval is None:
            nsample = 100
            rng = np.random.default_rng()
            idx_0 = rng.choice(range(len(self.points)-1), size=nsample)
            idx_1 = idx_0+1
            idx = np.asarray([[i,j] for i,j in zip(idx_0, idx_1) if (i not in idx_1 and j not in idx_0)])
            d_grid = np.linalg.norm(self.points[idx[:, 0]] - self.points[idx[:, 1]], axis=1)
            idx = idx[d_grid<1.2 * self.interval]
            d_vector = np.linalg.norm(self.vector[idx[:,0]]-self.vector[idx[:,1]], axis=1).mean()
            k = d_vector / self.interval
            self._vector_interval = np.min(k)
        return self._vector_interval

    @property
    def vector_unit(self):
        # 将 top 和 bridge site 的 vector 差异定义为unit_vector, 作为过滤格点的参考
        if self._unit_vector is None:
            unit_list = []
            vlen = self.vlen
            sc = [min(vlen,c) for s,c in self.species]
            v0 = np.concatenate(np.array([[np.inf]*c for c in sc]))
            for idx, s in enumerate(self.species):
                r = self.rsub[s[0]] + self.rads
                v1 = v0.copy()  # top
                idx0 = sum(sc[:idx])
                v1[idx0] = r
                v2 = v1.copy()  # bridge
                v2[idx0+1] = r
                vv1, vv2 = self._vectorize_func([v1, v2])
                unit_list.append(euclidean(vv1, vv2))
            self._unit_vector = min(unit_list)
        return self._unit_vector

    def get_near_index_from_xyz(self, xyz, dist_type='real'):
        """
        返回最近邻位点的格点序号。距离可以是向量距离，也可以是空间距离

        :param xyz: 位点坐标
        :param dist_type: 最近邻距离的类型，real: 直角坐标距离，vector：向量空间距离
        :return: (point_idx, distance)
        """
        xyz = np.atleast_2d(xyz)
        tree = self._get_grid_tree()
        dd, ii = tree.query(xyz, k=1)
        return ii

    def grid_sample(self, N=1, probability=None, **kwargs):
        """
        Warning: Obsoleted, replaced by Sampling class
        :param probability:
        :param N:
        :return:
        """
        if 'energy' in self.grid_property:
            points_idx = addition_samples(self, size=N, probability=probability, **kwargs)
        else:
            points_idx = InitialSampling(self).samples(size=N)
        return points_idx

    # TODO: 将中心重新映射回到Cartesian坐标 ：
        # 找到向量空间最紧邻的N个点，判断其实空间的距离是否小于 interval × 2，直到有三个点满足
        # 然后进行空间变换 A x M = B，M = B / A = B x A-1, R = V x M
        # 或者直接使用最近邻点的坐标

    def plot_cluster(self, figname=None):
        """
        :param figname:
        :return:
        """
        if figname is None:
            figname = 'site_cluster.png'
        print("Plot the site verctor and cluster ...")
        if self._pca:
            reduced_vector = self.vector[:,:2]
            sample_vector = self._sample_vector
        else:
            pca = PCA(n_components=2)
            pca.fit(self.vector)
            reduced_vector = pca.transform(self.vector)
            sample_vector = pca.transform(self._sample_vector)
        # Obtain labels for each point
        # plot in vector space
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        labels = None
        title = f"Vectors Sampling"
        if self._clusters:
            labels = self._clusters.labels_
            title = f"The site vector colored in {self._clusters.n_clusters} clusters"
        ax.scatter(reduced_vector[:, 0], reduced_vector[:, 1], c=labels, cmap=plt.cm.Paired)
        ax.scatter(sample_vector[:, 0],sample_vector[:, 1], marker="+", s=100, linewidths=2,
                   color="black", zorder=10)
        ax.set_title(title)
        fig.set_dpi(300)
        fig.set_size_inches(10, 10)
        figname1 = 'vector_' + figname
        fig.savefig(figname1, bbox_inches='tight')
        plt.cla()
        plt.close("all")

        # plot grid
        title = f"Grid Sampling"
        if self._clusters:
            labels = self._clusters.predict(self.vector)
            title = f"The site grid colored in {self._clusters.n_clusters} clusters"
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.scatter(self.points[:, 0], self.points[:, 1], c=labels, s=1, cmap=plt.cm.Paired)
        ax.scatter(self.sample_points[:, 0],self.sample_points[:, 1], marker="+", s=100, linewidths=2,
                   color="black", zorder=10)
        ax.set_title(title)
        fig.set_dpi(300)
        fig.set_size_inches(10, 10)
        figname2 = 'grid_' + figname
        fig.savefig(figname2, bbox_inches='tight')
        plt.cla()
        plt.close("all")


    def set_sample(self, sample_points, keep_old_sample=True):
        """
        手动设置采样格点，计算 self._sample_vector。z 坐标自动被忽略。
        :param keep_old_sample: 判断是否保留原有的采样的点
        :param sample_points:
        :return:
        """
        # 找到 points 对应的 z
        z = griddata(self.points[:, :2], self.points[:, 2], sample_points[:, :2])
        new_sample_points = sample_points.copy()
        new_sample_points[:, 2] = z
        # 计算 vector
        if self.subtype == 'slab':
            pbc = [True, True, False]
        elif self.subtype == 'cluster':
            pbc = [False, False, False]
        else:
            pbc = self.atoms.pbc
        DAga, Dga = get_distances(new_sample_points, self.atoms.positions,
                                  cutoff=self.rcutoff,
                                  cell=self.atoms.cell, pbc=pbc)
        # 计算 points 的 vector
        vector = self.vectorize(Dga=Dga, pca=self.lpca)
        if keep_old_sample and self.sample_points is not None:
            # 要判断 sample_property 的长度，来决定sample放到哪里
            if 'energy' in self.sample_property:
                len_value = len(self.sample_property['energy'])
            else:
                len_value = 0
            self.sample_points = np.concatenate([
                self.sample_points[:len_value],
                new_sample_points,
                self.sample_points[len_value:]
            ])
            self.sample_idx = np.concatenate([
                self.sample_idx[:len_value],
                [-1] * len(new_sample_points),  # 为新的插点赋值index -1, 作为区分
                self.sample_idx[len_value:]
            ])
            self._sample_vector = np.concatenate([
                self._sample_vector[:len_value],
                vector,
                self._sample_vector[len_value:]
            ])
        else:
            self.sample_points = new_sample_points
            self.sample_idx = np.array([-1] * len(new_sample_points))
            self._sample_vector = vector
            # 重置结果
            self.sample_property = {}

    def del_sample(self):
        self.sample_idx = None
        self._sample_vector = None
        self.sample_points = None
        self.sample_property = {}

    def set_property(self, values, key='energy'):
        """
        预测性质只能在能量之后，而且不支持迭代
        :param key:
        :param values:
        :return:
        """
        if key in self.sample_property:
            if len(self.sample_property[key]) == len(self._sample_vector):
                # 如果 _sample_vector 的长度与结果的长度相同，说明已经进行过回归，不需要再进行
                print("Warning: sample_vector 的长度与结果的长度相同，说明已经进行过回归，不需要再进行回归！")
                return None
            self.sample_property[key] = np.concatenate([self.sample_property[key], np.asarray(values)])
            if key == 'energy':
                self.iter += 1
        else:
            self.sample_property[key] = np.asarray(values)

        assert len(self._sample_vector) == len(self.sample_property[key])  # 这里需要保证采样的点来自于自主采样

        # Standardization of y
        scaler = StandardScaler()
        y = np.atleast_2d(self.sample_property[key]).T
        scaler.fit(y)
        y_scaled = scaler.transform(y).T[0]
        # RBF Kernel
        length_scale_grid = 1.0  # 实空间的length scale, 1 angstrom
        length_scale_vector = length_scale_grid * self._vector_interval
        length_scale_bounds = (length_scale_vector/2.0, length_scale_vector*2.0)
        # length_scale_bounds = 'fixed'
        # length_scale = [length_scale_vector] * self._vector_dim  # 向量空间的 length_scale, anisotropic
        length_scale = length_scale_vector  # 向量空间的 length_scale, isotropic
        rbf_kernel = RBF(length_scale=length_scale, length_scale_bounds=length_scale_bounds)
        # noise kernel
        noise_level_dict = {
            'energy': 0.01,  # eV
            'phi': 0.05,  # angle
        }
        if key in noise_level_dict:
            noise_level = noise_level_dict[key]  # eV
        else:
            noise_level = 0.001
        noise_level_norm = np.abs(noise_level / scaler.scale_[0])  # 标准化缩放
        white_kernel = WhiteKernel(noise_level=noise_level_norm, noise_level_bounds='fixed')
        # 总的 kernel
        constant_kernel = ConstantKernel(constant_value=1.0, constant_value_bounds='fixed')
        kernel = constant_kernel * rbf_kernel + white_kernel
        gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=9, alpha=noise_level_norm*0.01)
        print(f"Kernel parameters before fit:{kernel})")
        gp.fit(self._sample_vector, y_scaled)
        # 打印 GPR 结果
        print(f"Kernel parameters after fit: {gp.kernel_} \n"
              f"Log-likelihood: {gp.log_marginal_likelihood(gp.kernel_.theta):.3f}")
        # 为 self.points 插值
        y_predict_scaled, y_sigma_predict_scaled = gp.predict(self.vector, return_std=True)
        # 逆向求真实数值
        y_predict_scaled = np.atleast_2d(y_predict_scaled).T
        self.grid_property[key] = scaler.inverse_transform(y_predict_scaled).T[0]
        self.grid_property_sigma[key] = y_sigma_predict_scaled * np.abs(scaler.scale_[0])  # 误差不需要逆向求值，只需要系数

    def plot_property(self, key='energy', sample=True, figname=None, vmax=None, vmin=None):
        """
        TODO: 支持 cluster 作图。保存原始 meshgrid 和 id？或者重新插值？
        :param key: 画图的内容，对应于 grid_property 中的 key
        :param sample: 是否画上 sample 点，默认是
        :param figname: 图片名字，默认 key_iter_niter.png
        :param vmax: colorbar 最大值，默认自动
        :param vmin: colorbar 最小值，默认自动
        :return:
        """
        assert key in self.grid_property
        fig, ax = plt.subplots()
        ax.set_aspect('equal')

        print(f"Plot {key} ...")
        x = self.points[:, 0]
        y = self.points[:, 1]
        z = self.grid_property[key]
        triang = mtri.Triangulation(x, y)
        contourf0 = ax.tricontourf(triang, z, levels=50, cmap="jet", vmin=vmin, vmax=vmax)

        # 画上 sample 点，采过的点用黑色，下一步采的点用白色
        if sample:
            sample_points = self.sample_points
            nsampled = len(self.sample_property['energy'])
            ax.scatter(sample_points[0:nsampled, 0], sample_points[0:nsampled, 1], marker="+", s=100, linewidths=2,
                       color="black", zorder=10)
            ax.scatter(sample_points[nsampled:, 0], sample_points[nsampled:, 1], marker="o", s=100, linewidths=2,
                       color="w", zorder=10)
        fig.colorbar(contourf0, ax=ax)
        title = f"{key.capitalize()} distribution"
        if key in self.grid_property_sigma:
            title += f", Max(sigma)={self.grid_property_sigma[key].max():.3f}"
        ax.set_title(title)
        fig.set_dpi(300)
        fig.set_size_inches(10, 10)
        if figname is None:
            figname = key + '_iter' + str(self.iter) + '.png'
        fig.savefig(figname, bbox_inches='tight')

        plt.cla()
        plt.close("all")

    def set_energy(self, values):
        """
        TODO: 保留了以前的运行命令，但是其他参数都不起作用了
        TODO: 新的模块需要测试
        :param values:
        :return:
        """
        self.set_property(values)

    def plot_energy(self, figname=None, vmax=None, vmin=None):
        """
        TODO: 保留了以前的运行命令，但是其他参数都不起作用了
        TODO: 新的模块需要测试
        :param figname:
        :param vmax:
        :param vmin:
        :return:
        """
        self.plot_property(figname=figname, vmax=vmax, vmin=vmin)

    def line_profile(self, path=None, key='energy'):
        """
        画出给定路径的能量扫面曲线图
        :param path:
        :param key:
        :return:
        """
        if key not in self.grid_property:
            raise KeyError
        if len(path) < 2:
            raise ValueError
        # 路径格点
        line_points = None
        path_length = 0.0
        for i in range(1, len(path[1:])+1):
            length = euclidean(path[i], path[i-1])
            path_length += length
            n = int(length / self.interval) + 1
            x = np.linspace(path[i-1][0], path[i][0], n, endpoint=False)
            y = np.linspace(path[i-1][1], path[i][1], n, endpoint=False)
            if line_points is not None:
                line_points = np.concatenate([line_points, np.array([x, y]).T])
            else:
                line_points = np.array([x, y]).T
        line_points = np.concatenate([line_points, [path[-1]]])
        # 插值
        line_values = griddata(points=self.points[:, 0:2],
                               values=self.grid_property[key],
                               xi=line_points,
                               method='linear')

        line_x = np.linspace(0.0, path_length, len(line_values))
        return line_x, line_values

    def plot_sigma(self, key='energy', figname=None, vmax=None, vmin=None):
        # TODO: 支持 cluster 作图。保存原始 meshgrid 和 id？或者重新插值？
        assert key in self.grid_property_sigma
        fig, ax = plt.subplots()
        ax.set_aspect('equal')

        x = self.points[:, 0]
        y = self.points[:, 1]
        z = self.grid_property_sigma[key]
        triang = mtri.Triangulation(x, y)
        contourf0 = ax.tricontourf(triang, z, levels=50, cmap="RdPu", vmin=vmin, vmax=vmax)

        # sigma 最大值标注
        max_sigma_point = self.points[self.grid_property_sigma[key].argmax()]
        ax.scatter(max_sigma_point[0], max_sigma_point[1], marker="+", s=100, linewidths=2,
                   color="w", zorder=10)
        fig.colorbar(contourf0, ax=ax)
        title = f"Gaussian Process Error of {key.capitalize()}, Max(sigma)={self.grid_property_sigma[key].max():.3f} eV"
        ax.set_title(title)

        fig.set_dpi(300)
        fig.set_size_inches(10, 10)
        if figname is None:
            figname = key + '_sigma_iter' + str(self.iter) + '.png'
        fig.savefig(figname, bbox_inches='tight')
        plt.cla()
        plt.close("all")

    def error(self):
        """
        TODO: 改为 @property，默认返回无穷大
        TODO: 假设点越多，误差越小。计算倒数第二帧与最后一帧之间的平均误差或者方差
        TODO：输出前面不同帧的误差变化曲线
        :return:
        """
        if 'energy' in self.grid_property_sigma:
            return self.grid_property_sigma['energy'].max()
        else:
            print("No energy for points!")
            return None

    def to_pkl(self, pkl_file="surface_grid.pkl"):
        file_pi = open(pkl_file, 'wb')
        pickle.dump(self, file_pi)
        file_pi.close()

    @classmethod
    def from_pkl(cls, pkl_file="surface_grid.pkl"):
        filehandler = open(pkl_file, 'rb')
        obj = pickle.load(filehandler)
        filehandler.close()
        return obj


def combine_sg_vector(*sg_lst):
    """
    TODO: 使用 class 对多个 sg 进行管理，合并等等
    合并 sg.vector to a larger vector set, in order to plot it
    :param sg_lst:
    :return:
    """

    if len(sg_lst) == 0:
        return None
    elif len(sg_lst) == 1:
        return sg_lst[0]._raw_vector

    species_num_lst = sorted(set([s[0] for sg in sg_lst for s in sg.species]))
    species_default_dct = {num: 0 for num in species_num_lst}
    species_lsts = []
    vlen_max = species_default_dct.copy()
    for sg in sg_lst:
        species_dct = species_default_dct.copy()
        species_dct.update({num: min(sg.vlen, cnt) for num, cnt in sg.species})
        # 对 species_dcts 中的元素进行排序
        species_lst = sorted(species_dct.items(), key=lambda x: x[0])
        species_lsts.append(species_lst)
        vlen_max = {num: max(vlen_max[num], vlen) for num, vlen in species_dct.items()}  # 更新向量最大值
    # 对 vlen_max 进行排序

    new_vector_lst = []
    for sg, species_lst in zip(sg_lst, species_lsts):
        # 提取 raw_vector, 对不足的 vector 进行补齐
        raw_vector = sg._raw_vector
        nvector = len(raw_vector)  # 总行数
        pointer = 0  # 列指针
        new_vector = []
        for num, cnt in species_lst:
            new_vlen = vlen_max[num]
            new_v = np.zeros([nvector, new_vlen])
            new_v += 1.0 * raw_vector.min()  # 超过截断的使用最小值的三分之二，从而减小不同表面之间的结构差异
            # 判断长度是不是 0
            if cnt == 0:
                new_vector.append(new_v)
                continue
            # 取出对应的 vector 列
            old_v = raw_vector[:, pointer:pointer+cnt]
            # 判断是不是要补齐
            if cnt == new_vlen:
                new_vector.append(old_v)
            else:
                new_v[:, :cnt] = old_v
                new_vector.append(new_v)
            pointer += cnt
        new_vector = np.concatenate(new_vector, axis=1)
        new_vector_lst.append(new_vector)
    vector_combine = np.concatenate(new_vector_lst, axis=0)

    return vector_combine
