import main

def test_bubble_sort():
    array = [-2, 45, 0, 11, -9]
    assert main.bubble_sort(array) == [-9, -2, 0, 11, 45]

def test_optimised_bubble_sort():
    array = [-2, 45, 0, 11, -9]
    assert main.optimised_bubble_sort(array) == [-9, -2, 0, 11, 45]