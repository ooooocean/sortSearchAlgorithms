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

    def max_heapify(self, root):

        # add in checks for when there is less than 2 children
        left_val = root.left.value if root.left else 0
        right_val = root.right.value if root.right else 0

        print(f'for {root.value}, left child is {left_val} and right child is {right_val}')

        # in the terminal case, we make no changes
        if root.value > left_val and root.value > right_val:
            print(' no change, root is largest')
            return
        # if one of the children is larger, swap the values
        if right_val > root.value and right_val > left_val:
            (root.right.value, root.value) = (root.value, root.right.value)
            print(f'right value is bigger, we now have root = {root.value}, left = {root.left.value}, right={root.right.value}')
        if left_val > root.value and left_val > right_val:
            (root.left.value, root.value) = (root.value,root.left.value)
            print(f'left value is bigger, we now have root = {root.value}, left = {root.left.value}, right={root.right.value}')


        # regardless of any swaps, we need to heapify each of the subtrees to make sure that
        # heap property is maintained
        self.max_heapify(root.left)
        self.max_heapify(root.right)



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


x = [1,12,9,5,6,10]
# tree = Tree()
# tree.root = array_to_tree_2(x, tree.root,0)
# tree.print_helper(tree.root,'',False)
# print('\n')
# tree.max_heapify(tree.root)
# tree.print_helper(tree.root,'',False)

def heapify_array(array, n, i):
    for j in range(i, -1, -1):
        # set current value to be the largest
        largest = i

        # define left and right children
        left = (2 * i) + 1
        right = (2 * i) + 2

        if left < n and array[left] > array[largest]:
            largest = left
        if right < n and array[right] > array[largest]:
            largest = right
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            heapify_array(array, n, largest)
        i-=1

def heap_sort(array, n):
    print(f'input is {array}')
    for i in range(n-1):
        # remove root element and add to end of array
        array[0], array[n-1-i] = array[n-1-i], array[0]
        print(f'array elements swapped for i={i}\narray is now {array}')

        # heapify with reduced heap
        new_idx = (n // 2) - 1
        heapify_array(array, n-1-i, new_idx)
        print(f'array heapified to {array}\n')
    return array

def shell_sort(array, n):
    # define the interval - in this case, we are using the default
    interval = n // 2

    # we iterate until the interval is equal to 1
    while interval > 0:
        # on the inner loop, explicitly set n so that we don't include it
        for i in range(interval, n):
            # assign the further element to a var
            temp = array[i]
            j = i

            # we swap if the index is larger than the interval and the value is greater than the earlier element
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j-interval]
                j -= interval
            array[j] = temp
        interval //= 2


array = [9,8,3,7,5,6,4,1]
shell_sort(array, len(array))
print(array)