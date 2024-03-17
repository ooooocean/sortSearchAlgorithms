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

def test_partition():
    array = [8,7,6,1,0,9,2]
    assert main.partition(array, 0 , len(array)-1) == 2

def test_quick_sort():
    array = [8, 7, 6, 1, 0, 9, 2]
    main.quick_sort(array, 0, len(array)-1)
    assert array == [0,1,2,6,7,8,9]