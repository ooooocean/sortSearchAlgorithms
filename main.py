import sys


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

def count_sort_sig_fig(array, sigfig):
    # count sort that sorts based on significant figures

    size = len(array)
    output = [0] * size

    # since we are counting one column, we only need values 0 to 9
    count = [0] * 10

    # loop through input array and calculate count
    for i in range(0, size):
        # in order to get the correct column, we divide by the column (e.g. units, tenths)
        # then take the result and modulo 10
        index = ( array[i] // sigfig ) % 10
        count[index] += 1

    # calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i-1]

    # place elements in sorted order
    i = size - 1
    while i >= 0:
        index = ( array[i] // sigfig ) % 10
        output[count[index]-1] = array[i]
        count[index] -=1
        i-=1

    for i in range(0, size):
        array[i] = output[i]

def radix_sort(array):
    # find the max element and assign max no. of significant figures
    highest = max(array)

    sigfig = 1
    while highest // sigfig > 0:
        count_sort_sig_fig(array, sigfig)
        sigfig *= 10

def bucket_sort(array, no_of_buckets):
    # create bucket array
    buckets = []
    for i in range(no_of_buckets):
        buckets.append([])

    # determine bucket interval by
    interval = (max(array) - min(array)) / no_of_buckets
    # iterate through the array and add to bucket
    for i in range(len(array)-1):
        if array[i] == max(array):
            buckets[no_of_buckets-1].append(array[i])
        else:
            # find which interval the value lies in
            temp = (array[i] - min(array)) / interval
            position = int(temp)
            buckets[position].append(array[i])

    # now sort for each bucket
    for i in range(no_of_buckets):
        buckets[i].sort()
    output = []
    for i in range(no_of_buckets):
        for j in range(len(buckets[i])):
            output.append(buckets[i][j])
    return output


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def print_helper(self, currPtr, indent, last):
        if currPtr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.value)
            self.print_helper(currPtr.left, indent, False)
            self.print_helper(currPtr.right, indent, True)

def array_to_tree(array):
    for i in range(len(array)):
        temp = Node(array[i])

        if i == 0:
            tree = Tree()
            tree.root = temp

        left_ele_index = (2 * i) + 1
        right_ele_index = (2 * i) + 2

        if left_ele_index <= len(array)-1:
            temp.left = Node(array[left_ele_index])
        if right_ele_index <= len(array)-1:
            temp.right = Node(array[right_ele_index])
    return tree
# x=array_to_tree([1,12,9,5,6,10])
# x.print_helper(x.root,'',False)

def array_to_tree_2(array, root, i):
    # define terminal case
    if i >= len(array):
        return

    print(f'function called for index {i}')

    # assign value to root
    if i == 0:
        root = Node(array[i])

    # assign a left child its index exists in the array
    left_child_idx = (2*i) + 1

    if left_child_idx <= len(array) - 1:
        print(f'assigned element to index {left_child_idx}')
        root.left = Node(array[left_child_idx])
        array_to_tree_2(array, root.left, left_child_idx)

    # repeat for right child
    right_child_idx = (2*i) + 2
    if right_child_idx <= len(array) - 1:
        root.right = Node(array[right_child_idx])
        array_to_tree_2(array, root.right,right_child_idx)

    return root
