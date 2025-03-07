import numpy as np

from multipie2 import TOL, DIGIT
from multipie2.data.data_crystal import t_dict
from multipie2.util.util import str_to_sympy

SHIFT = 1.0 - TOL
TOL_SAME_SITE = 1e-8

t_dict = {lattice: None if t is None else str_to_sympy(t).astype(float) for lattice, t in t_dict.items()}


# ==================================================
def align_vector(vector, tol=TOL):
    """
    Align vector so that smallest non-zero component is in positive direction.

    Args:
        vector (array-like): set of vectors.
        tol (float, optional): tolerance for zero.

    Returns:
        - (ndarray) -- aligned set of vectors.
    """
    vector = np.asarray(vector, dtype=float)
    vector[np.abs(vector) < tol] = 0.0
    abs_vector = np.abs(vector)
    first_nonzero_idx = np.argmax(abs_vector > tol, axis=1)
    sign = np.sign(vector)
    flip_sign = np.take_along_axis(sign, first_nonzero_idx[:, None], axis=1).flatten()
    aligned_vector = vector * flip_sign[:, None]
    aligned_vector[np.abs(aligned_vector) < tol] = 0.0
    return aligned_vector


# ==================================================
def get_closest_vector(target, vec, tol=TOL):
    """
    Get closest vector.

    Args:
        target (array-like): vector.
        vec (array-like): list of vectors.
        tol (float, optional): absolute tolerance.

    Returns:
        - (int) -- index (when distance > tol, None).
    """
    target = np.asarray(target, dtype=float)
    vec = np.asarray(vec, dtype=float)

    distances = np.linalg.norm(vec - target, axis=1)
    idx = np.argmin(distances)
    if distances[idx] < tol:
        return idx
    else:
        return None


# ==================================================
def remove_duplicate_vector(vec, tol=TOL, directional=True):
    """
    Remove duplicate vector.

    Args:
        vec (array-like): list of vectors.
        tol (float, optional): absolute tolerance.
        directional (bool, optional): directional vector ?

    Returns:
        - (ndarray) -- vectors.

    Note:
        - each vector is assumed to be 3d vector or 6d bond (3d vector and 3d center).
    """
    vec = np.asarray(vec, dtype=float)

    vecs = []
    if directional:
        for v in vec:
            if not any(np.allclose(v, uniq_vec, atol=tol) for uniq_vec in vecs):
                vecs.append(v)
    else:
        for v in vec:
            nv = v.copy()
            nv[0:3] = -v[0:3]
            if not any(np.allclose(v, uniq_vec, atol=tol) for uniq_vec in vecs) and not any(
                np.allclose(nv, uniq_vec, atol=tol) for uniq_vec in vecs
            ):
                vecs.append(v)
    return np.array(vecs)


# ==================================================
def _create_equivalent(lattice, site_cf, so_cf, remove_duplicate, directional, plus_set=False, shift=False):
    """
    Create equivalent vector.

    Args:
        lattice (str): crystal lattice, (A/B/C/P/I/F/R/0). [0: point group].
        site_cf (array-like): site in conventional cell in fractional coordinate.
        so_cf (array-like): symmetry operation matrices in conventional cell in fractional coordinate.
        remove_duplicate (bool): remove duplicate vector ?
        directional (bool, optional): directional vector ?
        plus_set (bool, optional): add plus set for space group ?
        shift (bool, optional): shift to home unit cell for space group ?

    Returns:
        - (ndarray) -- equivalent vector.

    Note:
        - no shift and plus_set for point group.
    """
    so_cf = np.asarray(so_cf, dtype=float)
    site_cf = np.asarray(site_cf, dtype=float)

    if lattice == "0":  # point group.
        so_cf = so_cf[:, 0:3, 0:3]  # get 3x3 SO matrix.
        site_list_cf = (so_cf @ site_cf).round(DIGIT)
        if remove_duplicate:
            site_list_cf = remove_duplicate_vector(site_list_cf, TOL_SAME_SITE, directional)
        return site_list_cf

    if shift:
        site_cf = np.mod(site_cf, SHIFT)
    site_cf = np.pad(site_cf, (0, 1), constant_values=1.0)  # pad 4th component for 4x4 operation.
    site_list_cf = so_cf @ site_cf
    site_list_cf = site_list_cf[:, 0:3]  # convert to 3 component.

    if plus_set:
        t = t_dict[lattice]
        site_list_cf = np.concatenate([site_list_cf + i for i in t]).round(DIGIT)
    if shift:
        site_list_cf = np.mod(site_list_cf, SHIFT)
    if remove_duplicate:
        site_list_cf = remove_duplicate_vector(site_list_cf, TOL_SAME_SITE, directional)

    return site_list_cf


# ==================================================
def equivalent_site(lattice, site_cf, so_cf):
    """
    Create equivalent site from given site.

    Args:
        lattice (str): crystal lattice, (A/B/C/P/I/F/R/0). [0: point group].
        site_cf (array-like): site in conventional cell in fractional coordinate.
        so_cf (array-like): symmetry operation matrices in conventional cell in fractional coordinate.

    Returns:
        - (ndarray) -- equivalent sites including plus set in conventional cell in fractional coordinate.

    Note:
        - for space group, site is shifted within home unit cell, and with plus set.
    """
    return _create_equivalent(lattice, site_cf, so_cf, remove_duplicate=True, directional=True, plus_set=True, shift=True)


# ==================================================
def equivalent_bond(lattice, vector_cf, center_cf, so_cf, directional):
    """
    Create equivalent bond from given bond.

    Args:
        lattice (str): crystal lattice, (A/B/C/P/I/F/R/0). [0: point group].
        vector_cf (array-like): bond vector in conventional cell in fractional coordinate.
        center_cf (array-like): bond center in conventional cell in fractional coordinate.
        so_cf (array-like): symmetry operation matrices in conventional cell in fractional coordinate.
        directional (bool): directional bond ?

    Returns:
        - (ndarray) -- equivalent bond vectors including plus set in conventional cell in fractional coordinate.
        - (ndarray) -- equivalent bond centers including plus set in conventional cell in fractional coordinate.

    Note:
        - for space group, site is shifted within home unit cell, and with plus set.
    """
    vector_list = _create_equivalent(
        "0", vector_cf, so_cf, remove_duplicate=False, directional=False, plus_set=False, shift=False
    )
    center_list = _create_equivalent(
        lattice, center_cf, so_cf, remove_duplicate=False, directional=True, plus_set=False, shift=(lattice != "0")
    )

    bond_list = np.hstack((vector_list, center_list))
    bond_list = remove_duplicate_vector(bond_list, TOL_SAME_SITE, directional)
    vector_list = bond_list[:, 0:3]
    center_list = bond_list[:, 3:6]

    if lattice != "0":
        t = t_dict[lattice]
        center_list = np.concatenate([center_list + i for i in t]).round(DIGIT)
        center_list = np.mod(center_list, SHIFT)
        vector_list = np.tile(vector_list, (len(t), 1))

    return vector_list, center_list


def check_vec(vector, solution, v0):
    v0, v1, v2 = solution.values()
    pos = np.vectorize(lambda i: i.subs({"X": v0, "Y": v1, "Z": v2}))(vector).astype(float).round(DIGIT)
    idx = get_closest_vector(v0, pos, TOL_SAME_SITE)
    return idx is not None


# ==================================================
def _find_wyckoff_bond(vector_cf, center_cf, lattice, so_cf, wyckoff_cf):
    from multipie2.util.more.util_wyckoff import _find_wyckoff_position, find_wyckoff_xyz

    s_wp, s = _find_wyckoff_position(center_cf, lattice, so_cf, wyckoff_cf["site"])

    # equivalent sites.
    vector, center = equivalent_bond(lattice, vector_cf, center_cf, so_cf, False)
    n = len(vector)

    # candidate Wyckoff positions.
    wyckoff = wyckoff_cf["site"][s_wp]["bond"]
    wp_list = [wp for wp in wyckoff if int(wp.split("@")[0][:-1]) == n]

    # list of Wyckoff position sites.
    wp_pos_list = [
        np.vectorize(lambda i: i.subs({"X": "x", "Y": "y", "Z": "z"}))(wyckoff_cf["bond"][wp]["vector"]) for wp in wp_list
    ]

    # find Wyckoff position to match with given site.
    s0 = vector[0]
    for wp, pos_list in zip(wp_list, wp_pos_list):
        for pos in pos_list:
            sol, diff = find_wyckoff_xyz(pos, s0)
            if diff < TOL and check_vec(wyckoff_cf["bond"][wp]["vector"], sol, vector_cf):
                return s_wp, s, wp, np.asarray([p.subs(sol) for p in pos_list[0]], dtype=float)

    return s_wp, s, "-", np.asarray([0.0, 0.0, 0.0])


# ==================================================
# ==================================================
def test1():
    vec = [
        [-3.0, 2.0, 1.0],
        [0.0, -2.0, 3.0],
        [0.0, 0.0, -4.0],
        [5.0, -1.0, 2.0],
        [0.0, 0.0, 7.0],
        [1e-12, -2.0, 3.0],
        [-0.0, 0.0, -0.0],
    ]
    align_vec = align_vector(vec)
    print(align_vec)


def test2():
    vec = [
        [1.0000001, 2.0000001, 3.0000001],
        [-1.0000001, -2.0000001, -3.0000001],
        [4.0, 5.0, 6.0],
        [-4.0, -5.0, -6.0],
        [1.0000001, 2.0000001, 3.0000001],
        [1.0, -2.0, 3.0],
        [4.0, 5.0, 6.0],
        [-1.0, 2.0, -3.0],
    ]
    rm_vec = remove_duplicate_vector(vec, directional=False)
    print(rm_vec)


def test3():
    vec = [
        [1.0000001, 2.0000001, 3.0000001],
        [-1.0000001, -2.0000001, -3.0000001],
        [4.0, 5.0, 6.0],
        [-4.0, -5.0, -6.0],
        [1.0000001, 2.0000001, 3.0000001],
        [1.0, -2.0, 3.0],
        [4.0, 5.0, 6.0],
        [-1.0, 2.0, -3.0],
    ]
    idx = get_closest_vector([4, 5, 6], vec)
    print(idx)


if __name__ == "__main__":
    test1()
    test2()
    test3()
