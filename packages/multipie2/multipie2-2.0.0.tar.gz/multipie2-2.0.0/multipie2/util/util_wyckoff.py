import numpy as np
from itertools import product

from multipie2.util.util import replace
from multipie2.util.util_crystal import shift_site, shift_bond, convert_to_primitive, TOL_SAME_SITE, DIGIT


# ==================================================
def find_vector(target, vec):
    """
    Find vector (lowest index only).

    Args:
        target (array-like): vector.
        vec (array-like): list of vectors.

    Returns:
        - (int) -- index (when not found, return None).
    """
    target = np.asarray(target, dtype=float)
    vec = np.asarray(vec, dtype=float)

    for no, v in enumerate(vec):
        if np.allclose(v, target, atol=TOL_SAME_SITE):
            return no
    return None


# ==================================================
def remove_duplicate_vector(vec, directional=True):
    """
    Remove duplicate vector.

    Args:
        vec (array-like): list of vectors.
        directional (bool, optional): directional vector ?

    Returns:
        - (ndarray) -- vectors.

    Note:
        - each vector is assumed to be site(3d) or bond(6d, vector+center).
    """
    vec = np.asarray(vec, dtype=float)

    vecs = []
    if directional:
        for v in vec:
            if not any(np.allclose(v, uniq_vec, atol=TOL_SAME_SITE) for uniq_vec in vecs):
                vecs.append(v)
    else:
        for v in vec:
            nv = v.copy()
            nv[0:3] = -v[0:3]
            if not any(np.allclose(v, uniq_vec, atol=TOL_SAME_SITE) for uniq_vec in vecs) and not any(
                np.allclose(nv, uniq_vec, atol=TOL_SAME_SITE) for uniq_vec in vecs
            ):
                vecs.append(v)
    return np.asarray(vecs)


# ==================================================
def find_xyz(pos, site, var=["x", "y", "z"]):
    """
    Find match in pos for given site, and obtain [x,y,z].

    Args:
        pos (ndarray): set of vectors in terms of var.
        site (ndarray): site to match.
        var (list, optional): variable.

    Returns:
        - (dict) -- (x,y,z) value (return None when not found).
    """
    sc = np.zeros(3)
    sxyz = np.eye(3)

    site = np.asarray(site, dtype=float)
    pos = np.asarray(pos, dtype=object)

    sub_b = dict(zip(var, sc))
    b = np.asarray([p.subs(sub_b) for p in pos], dtype=float)
    sub_A = [dict(zip(var, si)) for si in sxyz]
    A = np.array([[p.subs(subs) for subs in sub_A] for p in pos - b], dtype=float)

    solution = np.linalg.lstsq(A, site - b, rcond=None)[0].tolist()
    solution = dict(zip(var, solution))

    sol_site = replace(pos, solution).astype(float)
    if not np.allclose(sol_site, site, atol=TOL_SAME_SITE):
        return None

    return solution


# ==================================================
def create_equivalent_site(so, s0, shift):
    """
    Create equivalent site for given site, s0 (with plus set).

    Args:
        so (ndarray): symmetry operation (primitive) (PG:3x3) or (SG:4x4).
        s0 (ndarray): representative site (float).
        shift (bool, optional): shift site for SG ?

    Returns:
        - (ndarray) -- set of equivalent site.
    """
    so = so.astype(float)

    if shift:
        site = (so @ np.pad(s0, (0, 1), constant_values=1))[:, 0:3]
        site = shift_site(site)
    else:
        site = so[:, 0:3, 0:3] @ s0

    site = remove_duplicate_vector(site)

    return site


# ==================================================
def create_equivalent_bond(so, so_p, b0, shift):
    """
    Create equivalent bond for given bond, v0@s0 (with plus set).

    Args:
        so (ndarray): symmetry operation (primitive) (PG:3x3) or (SG:4x4).
        b0 (ndarray): representative bond, (vector+center) (float).
        shift (bool, optional): shift center for SG ?
        pset (ndarray, optional): plus set, which must be given for SG.

    Returns:
        - (ndarray) -- set of equivalent bond (vector+center).
    """
    so = so.astype(float)
    so_p = so_p.astype(float)
    v0, s0 = b0[0:3], b0[3:6]

    vector = so[:, 0:3, 0:3] @ v0

    if shift:
        center = (so_p @ np.pad(s0, (0, 1), constant_values=1))[:, 0:3]
        center = shift_site(center)
    else:
        center = so_p[:, 0:3, 0:3] @ s0

    bond = np.hstack((vector[:, None], center[:, None])).reshape(-1, 6)
    bond = remove_duplicate_vector(bond, directional=False)

    return bond


# ==================================================
def wyckoff_site_for_search(site_ex):
    """
    Wyckoff site for search with surrounding cell (no plus set).

    Args:
        site_ex (ndarray): set of Wyckoff site in terms of (x,y,z).

    Returns:
        - (ndarray) -- set of Wyckoff site for search.
    """
    shift = np.array(list(product([-1, 0, 1], repeat=3)), dtype=object)
    pos = np.concatenate([site_ex + i for i in shift])
    return pos


# ==================================================
def wyckoff_bond_for_search(bond_ex):
    """
    Wyckoff bond for search with surrounding cell (no plus set).

    Args:
        bond_ex (ndarray): set of Wyckoff bond in terms of (X,Y,Z,x,y,z).

    Returns:
        - (ndarray) -- set of Wyckoff bond vector for search.
        - (ndarray) -- set of Wyckoff bond center for search.
    """
    vec, ctr = bond_ex[:, 0:3], bond_ex[:, 3:6]

    ctr = wyckoff_site_for_search(ctr)
    n = len(ctr) // len(bond_ex)
    vec = np.tile(vec, (n, 1))

    return vec, ctr


# ==================================================
def evaluate_wyckoff_site(wyckoff_site, xyz, pset=None):
    """
    Evaluate Wyckoff site for given site for x, y, z (with plus set).

    Args:
        wyckoff_site (ndarray): set of Wyckoff site in terms of (x,y,z).
        xyz (dict): x, y, z value dict.
        pset (ndarray, optional): plus set, which must be given for SG.

    Returns:
        - (ndarray) -- set of Wyckoff site (plus_set0, plus_set1, ...).
    """
    all_site = replace(wyckoff_site, xyz).astype(float)
    if pset is not None:
        pset = pset.astype(float)
        all_site = np.concatenate([all_site + i for i in pset])
        all_site = shift_site(all_site)

    return all_site


# ==================================================
def evaluate_wyckoff_bond(wyckoff_bond, XYZxyz, pset=None):
    """
    Evaluate Wyckoff bond for given bond for X, Y, Z, x, y, z (with plus set).

    Args:
        wyckoff_bond (ndarray): set of Wyckoff bond in terms of (X,Y,Z)@(x,y,z).
        XYZxyz (dict): X, Y, Z, x, y, z value dict.
        pset (ndarray, optional): plus set, which must be given for SG.

    Returns:
        - (ndarray) -- set of Wyckoff bond (vector+center) (plus_set0, plus_set1, ...).
    """
    all_bond = replace(wyckoff_bond, XYZxyz).astype(float)
    if pset is not None:
        pset = pset.astype(float)
        vec, ctr = all_bond[:, 0:3], all_bond[:, 3:6]
        ctr = np.concatenate([ctr + i for i in pset])
        ctr = shift_site(ctr)
        vec = np.tile(vec, (len(pset), 1))
        all_bond = np.hstack((vec[:, None], ctr[:, None])).reshape(-1, 6)

    return all_bond


# ==================================================
def _find_wyckoff_site_pg(so, wyckoff_site, site):
    """
    Find Wyckoff site for point group.

    Args:
        so (ndarray): symmetry operation (3x3).
        wyckoff_site (BinaryManager): Wyckoff site info. for given group.
        site (ndarray): site to find.

    Returns:
        - (str) -- Wyckoff position (return None when not found).
        - (dict) -- x, y, z value dict.
        - (ndarray) -- first Wyckoff site (return None when not found).
    """

    def solve():
        for wp in wp_list:
            wp_pos = wyckoff_site[wp]["expression"]
            for p in wp_pos:
                sol = find_xyz(p, site)
                if sol is None:
                    continue
                return wp, sol
        return None, None

    site_list = create_equivalent_site(so, site, shift=False)
    wp_list = [wp for wp in wyckoff_site.keys() if int(wp[:-1]) == len(site_list)]
    s_wp, sol = solve()
    if s_wp is None:
        return None, None, None
    sol = {k: round(v, DIGIT) for k, v in sol.items()}

    wyckoff_site_wp = wyckoff_site[s_wp]["expression"][0]
    s0 = replace(wyckoff_site_wp, sol).astype(float).round(DIGIT)

    return s_wp, sol, s0


# ==================================================
def _find_wyckoff_site_sg(so, wyckoff_site, site, lattice, pset):
    """
    Find Wyckoff site for space group.

    Args:
        so (ndarray): symmetry operation (4x4, primitive).
        wyckoff_site (BinaryManager): Wyckoff site (primitive) info. for given group.
        site (ndarray): site to find.
        lattice (str): lattice.
        pset (ndarray): plus set.

    Returns:
        - (str) -- Wyckoff position (return None when not found).
        - (dict) -- x, y, z value dict.
        - (ndarray) -- first Wyckoff site (return None when not found).
    """

    def solve():
        for wp in wp_list:
            wp_pos = wyckoff_site_for_search(wyckoff_site[wp]["primitive"])
            for p in wp_pos:
                sol = find_xyz(p, site_p)
                if sol is None:
                    continue
                return wp, sol
        return None, None

    site = shift_site(site).astype(float)
    site_p = convert_to_primitive(lattice, site, shift=True).astype(float)

    site_list = create_equivalent_site(so, site_p, shift=True)
    wp_list = [wp for wp in wyckoff_site.keys() if int(wp[:-1]) == len(pset) * len(site_list)]
    s_wp, sol = solve()
    if s_wp is None:
        return None, None, None
    sol = {k: round(v, DIGIT) for k, v in sol.items()}

    wyckoff_site_wp = wyckoff_site[s_wp]["expression"][0]
    s0 = shift_site(replace(wyckoff_site_wp, sol)).astype(float)

    return s_wp, sol, s0


# ==================================================
def find_wyckoff_site(g, site):
    """
    Find Wyckoff site.

    Args:
        g (BinaryManager): info. for given group.
        site (ndarray): site to find.

    Returns:
        - (str) -- Wyckoff position (return None when not found).
        - (dict) -- x, y, z value dict.
        - (ndarray) -- first Wyckoff site (return None when not found).
    """
    wyckoff_site = g["wyckoff"]["site"]
    lattice = g["info"]["lattice"]
    if lattice == "0":
        so = g["symmetry_operation"]["fractional"]
        return _find_wyckoff_site_pg(so, wyckoff_site, site)
    else:
        so = g["symmetry_operation"]["fractional_primitive"]
        pset = g["symmetry_operation"]["plus_set"]
        return _find_wyckoff_site_sg(so, wyckoff_site, site, lattice, pset)


# ==================================================
def _find_wyckoff_bond_pg(so, wyckoff_site, wyckoff_bond, bond):
    """
    Find Wyckoff bond for point group.

    Args:
        so (ndarray): symmetry operation (3x3).
        wyckoff_site (BinaryManager): Wyckoff site info. for given group.
        wyckoff_bond (BinaryManager): Wyckoff bond info. for given group.
        bond (ndarray): bond (vector+center) to find.

    Returns:
        - (str) -- Wyckoff bond position (return None when not found).
        - (dict) -- X, Y, Z, x, y, z value dict.
        - (ndarray) -- first Wyckoff bond (vector+center) (return None when not found).
    """

    def solve():
        for wp in wp_list:
            bond = wyckoff_bond[wp]["expression"]
            vec, ctr = bond[:, 0:3], bond[:, 3:6]
            for v, c in zip(vec, ctr):
                v_sol = find_xyz(v, vector, ["X", "Y", "Z"])
                if v_sol is None:
                    continue
                c_sol = find_xyz(c, center)
                if c_sol is None:
                    continue
                return wp, v_sol | c_sol
        return None, None

    vector, center = bond[0:3], bond[3:6]
    c_wp = _find_wyckoff_site_pg(so, wyckoff_site, center)[0]
    if c_wp is None:
        return None, None, None

    bond_list = create_equivalent_bond(so, so, bond, shift=False)
    wp_list = [wp for wp in wyckoff_site[c_wp]["bond"] if int(wp.split("@")[0][:-1]) == len(bond_list)]
    b_wp, sol = solve()
    if b_wp is None:
        return None, None, None, None
    sol = {k: round(v, DIGIT) for k, v in sol.items()}

    wyckoff_bond_wp = wyckoff_bond[b_wp]["expression"][0]
    b0 = replace(wyckoff_bond_wp, sol).astype(float).round(DIGIT)

    return b_wp, sol, b0


# ==================================================
def _find_wyckoff_bond_sg(so, so_p, wyckoff_site, wyckoff_bond, bond, lattice, pset):
    """
    Find Wyckoff bond for space group.

    Args:
        so (ndarray): symmetry operation (4x4, conventional).
        so_p (ndarray): symmetry operation (4x4, primitive).
        wyckoff_site (BinaryManager): Wyckoff site info. for given group.
        wyckoff_bond (BinaryManager): Wyckoff bond info. for given group.
        bond (ndarray): bond (vector+center) to find.
        lattice (str): lattice.
        pset (ndarray): plus set.

    Returns:
        - (str) -- Wyckoff bond position (return None when not found).
        - (dict) -- X, Y, Z, x, y, z value dict.
        - (ndarray) -- first Wyckoff bond (vector+center) (return None when not found).
    """

    def solve():
        for wp in wp_list:
            vec, ctr = wyckoff_bond_for_search(wyckoff_bond[wp]["primitive"])
            for v, c in zip(vec, ctr):
                v_sol = find_xyz(v, vector, ["X", "Y", "Z"])
                if v_sol is None:
                    continue
                c_sol = find_xyz(c, center_p)
                if c_sol is None:
                    continue
                return wp, v_sol | c_sol
        return None, None

    vector, center = bond[0:3], bond[3:6]
    vector = vector.astype(float)
    center = shift_site(center).astype(float)
    center_p = convert_to_primitive(lattice, center, shift=True).astype(float)
    bond_p = np.concatenate([vector, center_p])

    c_wp = _find_wyckoff_site_sg(so_p, wyckoff_site, center, lattice, pset)[0]
    if c_wp is None:
        return None, None, None

    bond_list = create_equivalent_bond(so, so_p, bond_p, shift=True)
    wp_list = [wp for wp in wyckoff_site[c_wp]["bond"] if int(wp.split("@")[0][:-1]) == len(pset) * len(bond_list)]
    b_wp, sol = solve()
    if b_wp is None:
        return None, None, None
    sol = {k: round(v, DIGIT) for k, v in sol.items()}

    wyckoff_bond_wp = wyckoff_bond[b_wp]["expression"][0]
    b0 = shift_bond(replace(wyckoff_bond_wp, sol))

    return b_wp, sol, b0


# ==================================================
def find_wyckoff_bond(g, bond):
    """
    Find Wyckoff bond.

    Args:
        g (BinaryManager): info. for given group.
        bond (ndarray): bond (vector+center) to find.

    Returns:
        - (str) -- Wyckoff bond position (return None when not found).
        - (dict) -- X, Y, Z, x, y, z value dict.
        - (ndarray) -- first Wyckoff bond (vector+center) (return None when not found).
    """
    wyckoff_site = g["wyckoff"]["site"]
    wyckoff_bond = g["wyckoff"]["bond"]
    lattice = g["info"]["lattice"]
    if lattice == "0":
        so = g["symmetry_operation"]["fractional"]
        return _find_wyckoff_bond_pg(so, wyckoff_site, wyckoff_bond, bond)
    else:
        so = g["symmetry_operation"]["fractional"]
        so_p = g["symmetry_operation"]["fractional_primitive"]
        pset = g["symmetry_operation"]["plus_set"]
        return _find_wyckoff_bond_sg(so, so_p, wyckoff_site, wyckoff_bond, bond, lattice, pset)
