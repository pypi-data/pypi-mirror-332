import numpy as np
import sympy as sp

from multipie2.util.util import replace
from multipie2.util.util_crystal import shift_site

# ==================================================
# vector direction source.
_vector_source = {
    # Ci : remove opposite direction.
    "triclinic": ["[X,Y,Z]"],
    # C2h : remove opposite direction.
    "monoclinic": ["[X,Y,Z]", "[X,0,Z]", "[0,Y,0]"],  # Y=0, X=Z=0.
    # D2h : remove opposite direction, x:-x, y:-y, z:-z.
    "orthorhombic": [
        "[X,Y,Z]",
        "[X,Y,0]",  # Z=0.
        "[X,0,Z]",  # Y=0.
        "[0,Y,Z]",  # X=0.
        "[0,0,Z]",  # X=Y=0.
        "[0,Y,0]",  # X=Z=0.
        "[X,0,0]",  # Y=Z=0.
    ],
    # D4h : remove opposite direction, x:-x, y:-y, z:-z, x:y.
    "tetragonal": [
        "[X,Y,Z]",
        #
        "[X,0,Z]",  # Y=0.
        "[0,X,Z]",
        #
        "[X,X,Z]",  # Y=X.
        "[X,-X,Z]",
        #
        "[X,Y,0]",  # Z=0.
        #
        "[X,0,0]",  # Y=Z=0.
        "[0,X,0]",
        #
        "[X,X,0]",  # Z=0.
        "[X,-X,0]",
        #
        "[0,0,Z]",  # X=Y=0.
    ],
    # D3d, D3d-1 : remove opposite direction, x:-x, y:-y, z:-z.
    "trigonal": [
        "[X,Y,Z]",
        #
        "[X,0,Z]",  # Y=0, D3d.
        "[0,X,Z]",
        "[X,X,-Z]",
        #
        "[X,-X,Z]",  # Y=-X, D3d-1.
        "[X,2X,Z]",
        "[2X,X,-Z]",
        #
        "[X,-X,0]",  # Y=-X, Z=0, D3d.
        "[X,2X,0]",
        "[2X,X,0]",
        #
        "[X,0,0]",  # Y=Z=0, D3d-1.
        "[0,X,0]",
        "[X,X,0]",
        #
        "[0,0,Z]",  # X=Y=0.
    ],
    # D6h : remove opposite direction, x:-x, y:-y, z:-z, x:y.
    "hexagonal": [
        "[X,Y,Z]",
        #
        "[X,Y,0]",  # Z=0.
        "[X-Y,-Y,0]",
        "[X,X-Y,0]",
        #
        "[X,2X,Z]",  # Y=2X.
        "[X,-X,Z]",
        "[2X,X,Z]",
        #
        "[X,0,Z]",  # Y=0.
        "[0,X,Z]",
        "[X,X,Z]",
        #
        "[X,2X,0]",  # Y=2X, Z=0.
        "[X,-X,0]",
        "[2X,X,0]",
        #
        "[X,0,0]",  # Y=Z=0.
        "[0,X,0]",
        "[X,X,0]",
        #
        "[0,0,Z]",
    ],
    # Oh : remove opposite direction, x:-x, y:-y, z:-z, y:z.
    "cubic": [
        "[X,Y,Z]",
        #
        "[X,X,Z]",  # Y=X.
        "[X,Z,X]",
        "[Z,X,X]",
        "[X,-X,Z]",
        "[X,Z,-X]",
        "[Z,X,-X]",
        #
        "[0,Y,Z]",  # X=0.
        "[Y,0,Z]",
        "[Y,Z,0]",
        #
        "[X,X,0]",  # Y=X, Z=0.
        "[X,0,X]",
        "[0,X,X]",
        "[X,-X,0]",
        "[X,0,-X]",
        "[0,X,-X]",
        #
        "[X,X,X]",  # Y=Z=X.
        "[X,X,-X]",
        "[X,-X,X]",
        "[-X,X,X]",
        #
        "[X,0,0]",  # Y=Z=0.
        "[0,X,0]",
        "[0,0,X]",
    ],
}


# ==================================================
def align_vector(v):
    """
    Align vector (first non-zero component is set as positive).

    Args:
        v (ndarray): vector (3d vector or 6d bond, vector+center).

    Returns:
        - (ndarray) -- aligned vector.
    """
    sub = {"X": 7, "Y": 3, "Z": 1}  # dummy values in order to evaluate sign of each component.

    def is_regular_vector(v):
        vv = replace(v, sub)
        return next((i > 0 for i in vv if i != 0), True)

    vec, other = v[0:3], v[3:]  # accept both for vector and bond.
    return v if is_regular_vector(vec) else np.concatenate([-vec, other])


# ==================================================
def add_plus_set(vs, cs, pset):
    """
    Add plus set.

    Args:
        vs (ndarray): wyckoff vector in order of symmetry operation.
        cs (ndarray): wyckoff center in order of symmetry operation.
        pset (ndarray, optional): plus set (None for point group).

    Returns:
        - (ndarray) -- set of applied bond (shifted for space group, with plus set).
    """
    if pset is not None:
        cs = np.concatenate([cs + i for i in pset])
        cs = shift_site(cs)
        vs = np.tile(vs, (len(pset), 1))

    bs = np.hstack((vs[:, None], cs[:, None])).reshape(-1, 6)

    return bs


# ==================================================
def unique_vector(vs, sort):
    """
    Unique vector (align and remove duplicate).

    Args:
        vs (ndarray): set of vectors.
        sort (bool): sort vector ?

    Returns:
        - (ndarray) -- unique set of vector.
    """
    vs = [align_vector(i) for i in vs]  # align vectors or bonds.
    rvs = np.asarray(list(dict.fromkeys(map(tuple, vs))))  # remove duplicates.
    if sort:
        rvs = np.asarray(sorted(rvs, key=str))
    return rvs


# ==================================================
def regularize_mapping(cl, mapping):
    """
    Regularize mapping (first index is set as positive, and sort).

    Args:
        cl (ndarray): cluster set.
        mapping (list): mapping.

    Returns:
        - (ndarray) -- regularized cluster set.
        - (list) -- regularized mapping.
    """
    mapping = np.asarray(mapping, dtype=int)
    for i in range(len(mapping)):
        if mapping[i, 0] < 0:
            cl[i, 0:3] = -cl[i, 0:3]
            mapping[i] = -mapping[i]

    idx = np.argsort(mapping[:, 0])
    s_cl = cl[idx]
    s_mapping = mapping[idx].tolist()
    return s_cl, s_mapping


# ==================================================
def apply_so_vector(so, v0):
    """
    Apply SO to vector.

    Args:
        so (ndarray): set of symmetry operation.
        v0 (ndarray): source vector.

    Returns:
        - (ndarray) -- set of applied vector.
    """
    vs = so[:, 0:3, 0:3] @ v0
    return vs


# ==================================================
def vector_cluster_mapping(so, v0):
    """
    Create vector cluster mapping.

    Args:
        so (ndarray): set of symmetry operation.
        v0 (ndarray): source vector.

    Returns:
        - (ndarray) -- vector cluster set.
        - (list) -- SO mapping to cluster.
    """
    vs = apply_so_vector(so, v0)
    uvs = unique_vector(vs, sort=True)
    vs = apply_so_vector(so, uvs[0])

    mapping = [[] for _ in range(len(uvs))]
    for no, vi in enumerate(vs):
        for cno, i in enumerate(uvs):
            if (i == vi).all():
                mapping[cno].append(no + 1)
            elif (i == -vi).all():
                mapping[cno].append(-(no + 1))
    uvs, mapping = regularize_mapping(uvs, mapping)
    return uvs, mapping


# ==================================================
def vector_cluster_wp(source, so, site_mapping):
    """
    Create vector cluster for given wyckoff.

    Args:
        source (ndarray): set of source vector.
        so (ndarray): set of symmetry operation.
        site_mapping(ndarray): site mapping.

    Returns:
        - (list) -- set of source vector, mapping, vector cluster.
    """
    # set of symmetry operation for first Wyckoff site.
    so0 = np.asarray([so[i - 1] for i in site_mapping[0]])

    # unique mapping.
    unique_source = []
    vc_chk = []
    for v0 in source:
        vs, mp = vector_cluster_mapping(so0, v0)
        if str(mp) not in vc_chk:
            vc_chk.append(str(mp))
            unique_source.append((mp, v0, vs))
    unique_source = sorted(unique_source, reverse=True)  # sort by directional and non-directional vector.
    unique_source = sorted(unique_source, key=lambda i: len(i[0]))  # sort by size of vector cluster.
    unique_source = [(v0, mp, vs) for mp, v0, vs in unique_source]

    return unique_source


# ==================================================
def apply_so_bond(so, v0, cs, pset=None):
    """
    Apply SO to bond.

    Args:
        so (ndarray): set of symmetry operation.
        v0 (ndarray): source vector.
        cs (ndarray): wyckoff site in order of symmetry operation.
        pset (ndarray, optional): plus set (None for point group).

    Returns:
        - (ndarray) -- set of applied bond (shifted for space group, with plus set).
    """
    vs = so[:, 0:3, 0:3] @ v0
    bs = add_plus_set(vs, cs, pset)
    return bs


# ==================================================
def bond_cluster_mapping(so, v0, cs, pset=None):
    """
    Create bond cluster mapping.

    Args:
        so (ndarray): set of symmetry operation.
        v0 (ndarray): source vector.
        cs (ndarray): wyckoff site in order of symmetry operation.
        pset (ndarray, optional): plus set (None for point group).

    Returns:
        - (ndarray) -- bond cluster set.
        - (list) -- SO mapping to cluster.
    """
    bs = apply_so_bond(so, v0, cs, pset)
    ubs = unique_vector(bs, sort=False)

    mapping = [[] for _ in range(len(ubs))]
    for no, bi in enumerate(bs):
        for cno, i in enumerate(ubs):
            if (i == bi).all():
                mapping[cno].append(no + 1)
            elif (i == np.concatenate([-bi[0:3], bi[3:6]])).all():
                mapping[cno].append(-(no + 1))
    ubs, mapping = regularize_mapping(ubs, mapping)
    return ubs, mapping


# ==================================================
def bond_cluster_wp(vc_wp, so, cs, pset=None):
    """
    Create bond cluster and mapping for given wyckoff.

    Args:
        vc_wp (ndarray): vector cluster for given wyckoff.
        so (ndarray): set of symmetry operation.
        cs (ndarray): wyckoff site in order of symmetry operation.
        pset (ndarray, optional): plus set (None for point group).

    Returns:
        - (list) -- set of mapping and bond cluster (id of SO starts from one, no plus set).
    """
    # unique bond cluster.
    x, y, z = sp.symbols("x y z", real=True)
    sub_pg = [{"x": -x}, {"y": -y}, {"z": -z}]
    sub_sg = [
        {"x": sp.S(1) / 2 + x},
        {"x": sp.S(1) / 2 - x},
        {"x": sp.S(1) / 4 - x},
        {"x": sp.S(3) / 4 - x},
        {"z": sp.S(1) / 2 + z},
        {"z": sp.S(1) / 2 - z},
        {"z": sp.S(3) / 4 - z},
    ]
    npset = 1 if pset is None else len(pset)

    unique_bond = []
    bc_chk = []
    for v0, _, _ in vc_wp:
        bs = apply_so_bond(so, v0, cs, pset)
        bs0 = unique_vector(bs, sort=True)
        if pset is None:
            bss = [unique_vector(replace(bs0, d), sort=True) for d in sub_pg]
        else:
            bss = [unique_vector(shift_site(replace(bs0, d)), sort=True) for d in sub_pg + sub_sg]
        if str(bs0.tolist()) not in bc_chk:
            bc_chk.append(str(bs0.tolist()))
            for i in bss:
                bc_chk.append(str(i.tolist()))
            unique_bond.append((len(bs0), v0))
    unique_bond = sorted(unique_bond, key=lambda i: i[0])  # sort by size of cluster.

    # unique mapping.
    bc = []
    chk_mp = []
    for _, v0 in unique_bond:
        bs, mp = bond_cluster_mapping(so, v0, cs, pset)
        if str(mp) not in chk_mp:
            chk_mp.append(str(mp))
            size = len(bs) // npset
            bc.append((mp[:size], bs[:size]))

    bc = sorted(bc, reverse=True)  # sort by directional and non-directional bond.
    bc = sorted(bc, key=lambda i: len(i[0]))  # sort by size of bond cluster.

    return bc
