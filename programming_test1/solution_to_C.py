"""
C. Write a ​rotate(A, k) ​function which returns a rotated array A, k times; that is, each
element of A will be shifted to the right k times
○
rotate([3, 8, 9, 7, 6], 3) returns [9, 7, 6, 3, 8]
○
rotate([0, 0, 0], 1) returns [0, 0, 0]
○
rotate([1, 2, 3, 4], 4) returns [1, 2, 3, 4]
"""
from typing import List


def rotated_array(input_arr: List[int], key) -> List[int]:
    return input_arr[-key:] + input_arr[:-key]


if __name__ == "__main__":
    print(rotated_array([3, 8, 9, 7, 6], 3))
