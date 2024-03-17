def bubble_sort(array):
    # define the first step
    n = 0

    # assign the length of the array to a var
    length = len(array)

    # we always iterate until
    for n in range(length - 1):

        # iterate over the array, whose length is determined by length-1 subtracted by
        # the value of n, (number of largest elements)
        for i in range(length - 1 - n):
            # assign the ith element to a var
            first = array[i]
            second = array[i + 1]
            if first > second:
                array[i + 1] = first
                array[i] = second
            i += 1
        n += 1
    return array


def optimised_bubble_sort(array):
    # define the first step
    n = 0

    # assign the length of the array to a var
    length = len(array)

    # initialise the swapped var
    swapped = False

    # initialise step of array
    for n in range(length - 1):
        for i in range(length - 1 - n):
            first = array[i]
            second = array[i + 1]
            if first > second:
                array[i + 1] = first
                array[i] = second
                # since there is swapping, we set swapped to True
                swapped = True
            i += 1
        # after iterating through all elements, check if the array before is
        # the same as the array after
        if swapped is False:
            return array
    return array


def selection_sort(array):
    length = len(array)  # assign length of array to var

    for n in range(length - 1):
        minimum = n
        for i in range(n, length - 1, 1):  # start from the new index
            if array[minimum] > array[i + 1]:
                minimum = i + 1
        # once end of array reached, reassign start and end
        array[n], array[minimum] = array[minimum], array[n]
        n += 1
    return array


def insertion_sort(array):
    # start loop at step = 1
    for step in range(1, len(array)):
        value = array[step]
        # we init index var to compare previous values to current value
        idx = step - 1
        # loop through
        while idx >= 0 and value < array[idx]:
            array[idx + 1] = array[idx]
            idx -= 1
        array[idx + 1] = value
    return array

# define helper function that merges array after merge sort
def merge(array, p, q, r):
    # p and q determine subarray 1, where as q+1 and r determine subarray 2
    # to merge these into a sorted array, first write the subarrays to a variable
    subarray_1 = array[p:q+1:]
    subarray_2 = array[q+1:r+1:]
    # assign pointers for each of the arrays
    idx_sub_1 = idx_sub_2 = idx_main = 0

    # iterate until one subarray is complete
    while idx_sub_1 != len(subarray_1) and idx_sub_2 != len(subarray_2):
        # we add from subarray 1 if this element is larger, or the second subarray is iterated
        if subarray_1[idx_sub_1] < subarray_2[idx_sub_2]:
            array[idx_main] = subarray_1[idx_sub_1]
            idx_sub_1 += 1
            idx_main += 1
        if subarray_2[idx_sub_2] < subarray_1[idx_sub_1]:
            array[idx_main] = subarray_2[idx_sub_2]
            idx_sub_2 += 1
            idx_main += 1

    # if subarray 1 is complete, iterate through second subarray
    while idx_sub_1 != len(subarray_1):
        array[idx_main] = subarray_1[idx_sub_1]
        idx_sub_1 += 1
        idx_main +=1

    # repeat likewise for subarray 2
    while idx_sub_2 != len(subarray_2):
        array[idx_main] = subarray_2[idx_sub_2]
        idx_sub_2 += 1
        idx_main += 1

    return array



def merge_sort(array, p, r):
    # define the terminal case
    if p > r:
        return

    # find the midpoint of the input array. we always assign this to an int to drop the decimal
    q = int((p + r) / 2)

    # recurse function into first half
    merge_sort(array[p:q+1:], p, q)
    # recurse function into second half
    merge_sort(array[q+1:r+1], q+1, r)
    # we reach merge stage when a sub-array has a length 1
    # merge(array, p, q, r)
