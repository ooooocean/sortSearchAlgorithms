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
            if array[minimum] > array[i+1]:
                minimum = i+1
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
            array[idx+1] = array[idx]
            idx -= 1
        array[idx+1] = value
    return array

def partition(array, low, high):
    # function to swap the first instance of an element larger than pivot
    # with the first instance of an element smaller than pivot

    pivot = array[high]     # rightmost element as pivot
    i = low - 1             # pointer for greater element, -1 for initial call

    # traverse through all elements
    for j in range(low, high):
        # if the element at index is smaller than pivot, swap elements
        if array[j] <= pivot:
            i += 1          #
            (array[i], array[j]) = (array[j], array[i])

    # once all elements traverse, swap pivot element with greater element pointer
    (array[i+1], array[high]) = (array[high], array[i+1])

    # return position where partition is done
    return i+1

def quick_sort(array, low, high):
    # we terminate recursion once array is of size 1, i.e. index of low and high are same
    if low < high:

        #find the pivot element
        pivot_idx = partition(array, low, high)

        # recursively call the left partition
        quick_sort(array, low, pivot_idx-1)

        #recursively call the right parition
        quick_sort(array, pivot_idx+1, high)

def count_sort(array):
    # find max element of the array
    max_ele = max(array)

    # initialise the count array
    count_arr = [0] * (max_ele+1)

    # loop through the input array and calculate the count
    for i in range(len(array)):
        count_arr[array[i]] += 1
    print(count_arr)

    # convert count array into a cumulative count
    sum = 0
    for j in range(0, max_ele+1):
        sum += count_arr[j]
        count_arr[j] = sum
    print(count_arr)

    # assign output
    output = [None] * len(array)
    for k in range(len(array)):
        # take the value of the element from input and find the value for this in the count array
        output_index = count_arr[array[k]] - 1

        # reassign the new value to count_arr and create output var
        output[output_index] = array[k]
        count_arr[array[k]] -= 1

    return output
array =[4,2,2,8,3,3,1]
print(count_sort(array))
