def bubble_sort(array):
    # define the first step
    n = 0

    # assign the length of the array to a var
    length = len(array)

    # we always iterate until
    for n in range(length-1):

        # iterate over the array, whose length is determined by length-1 subtracted by the value of n,
        # (number of largest elements)
        for i in range(length-1-n):
            # assign the ith element to a var
            first = array[i]
            second = array[i+1]
            if first > second:
                array[i+1] = first
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
    for n in range(length-1):
        temp = array
        for i in range(length-1-n):
            first = array[i]
            second = array[i+1]
            if first > second:
                array[i+1] = first
                array[i] = second
                # since there is swapping, we set swapped to True
                swapped = True
            i += 1
        # after iterating through all elements, check if the array before is the same as the array after
        if swapped is False:
            return array
    return array