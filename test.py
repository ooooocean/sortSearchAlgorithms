import main

def test_bubble_sort():
    array = [-2, 45, 0, 11, -9]
    assert main.bubble_sort(array) == [-9, -2, 0, 11, 45]

def test_optimised_bubble_sort():
    array = [-2, 45, 0, 11, -9]
    assert main.optimised_bubble_sort(array) == [-9, -2, 0, 11, 45]

def test_selection_sort():
    array = [20, 12, 10, 15, 2]
    assert main.selection_sort(array) == [2, 10, 12, 15, 20]

def test_insertion_sort():
    array = [9, 5, 1, 4, 3]
    assert main.insertion_sort(array) == [1, 3, 4, 5, 9]


def test_merge():
    # array = [7, 3]
    # assert main.merge(array) == [3,7]
    #
    # array = [5,6,2,4]
    # assert main.merge(array) == [2,4,5,6]
    #
    # array = [2, 25]
    # assert main.merge(array) == [2,25]

    array = [347,699,420]
    assert main.merge(array, p = 0, r=0, q=len(array) // 2) == [347,420,699]

def test_merge_sort():
    array = [347,699,420]
    assert main.merge_sort(array, 0, len(array)) == [347,420,699]

    # array = [2,25,17,322,496,512,347,699,420]
    # assert main.merge_sort(array, 0, len(array)) == [2,17,25,322,347,420,496,512,699]