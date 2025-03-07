import numpy as np

from multipie2.util.more.util_more import convert_to_vector, sort_vector


# ==================================================
def test_convert_to_vector():
    print("=== test_convert_to_vector ===")
    s = ["(x+2y)/3", "0"]
    for i in s:
        v = convert_to_vector(i)
        print(i, "=>", v)


# ==================================================
def test_sort_vector():
    print("=== test_sort_vector ===")
    v = np.array([[1 / 3, 1 / 3, 0], [-1 / 3, 0, 0], [1 / 3, 1 / 2, 0], [1 / 3, 0, 1 / 2]])
    print(v)
    print()
    print(sort_vector(v))


# ==================================================
test_convert_to_vector()
test_sort_vector()
