"""
Write a function that computes square roots of numbers in a list.
Use this function to calculate square roots of the values in the given lists.
Write a test to confirm that your function works correctly.
"""
values1 = [1, 4, 3.14, 0, 0.001]
values2 = [0, -1, -2]


import math

def compute_square_roots(numbers):
    """
    Computes square roots of numbers in a list.
    Returns a new list with the computed square roots.
    """
    result = []
    for num in numbers:
        if num >= 0:
            result.append(math.sqrt(num))
        else:
            result.append(None)
    return result

# Testing the function with the given lists
print(compute_square_roots(values1))
print(compute_square_roots(values2))

#Test

# Testing the function with some test cases
def test_compute_square_roots():
    assert compute_square_roots([1, 4, 3.14, 0, 0.001]) == [1.0, 2.0, 1.77200451467, 0.0, 0.0316227766017]
    assert compute_square_roots([0, -1, -2]) == [0.0, None, None]
    assert compute_square_roots([]) == []
    assert compute_square_roots([-4]) == [None]
    assert compute_square_roots([25, 36, 49]) == [5.0, 6.0, 7.0]
    print("All tests pass")

test_compute_square_roots()
