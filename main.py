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