"""
A. Given an array A of N integers, write a function ​missing_int(A) ​that returns the smallest
positive integer (greater than 0) that does not occur in A.
○
A = [1, 3, 6, 4, 1, 2] should return 5
○
A = [1, 2, 3] should return 4
○
A = [-1, -1, -1, -5] should return 1
○
A = [1, 3, 6, 4, 1, 7, 8, 10] should return 2
"""
from typing import List


def smallest_positive_int(int_arr: List[int]) -> int:
    int_set = set(int_arr)

    compare_set = set(range(min(int_arr), max(int_arr)+1))

    diff = compare_set.difference(int_set)

    print(int_set)
    print(compare_set)
    print(diff)

    if not diff:
        return max(int_set) + 1
    elif next(iter(diff)) < 0:
        return 1
    else:
        return next(iter(diff))


if __name__ == "__main__":
    sample = [-1, -1, -1, -5]
    print(smallest_positive_int(sample))
