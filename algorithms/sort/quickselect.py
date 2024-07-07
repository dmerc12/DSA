'''
    Quickselect Algorithm
    --------------------------------------------------------------------
    Similar to quicksort but after sorting it selects the kth smallest element in a list.

    Time Complexity: Quadratic
    Time Complexity Notation: O(N^2)

    Space Complexity: Constant
    Space Complexity Notation: O(1)
    -------------------------------
'''

def partition(list, start_index, end_index):
    # Select the middle value as the pivot
    midpoint = start_index + (end_index - start_index) // 2
    pivot = list[midpoint]

    # "low" and "high" start at the ends of the list segment and move towards each other
    low = start_index
    high = end_index

    done = False
    while not done:
        # Increment low while list[low] < pivot
        while list[low] < pivot:
            low = low + 1

        # Decrement high while pivot < list[high]
        while pivot < list[high]:
            high = high - 1

        # If low and high have crossed each other, the loop is done. If not, the elements are swapped, low is incremented and high is decremented
        if low >= high:
            done = True
        else:
            temp = list[low]
            list[low] = list[high]
            list[high] = temp
            low = low + 1
            high = high - 1

    # "high" is the last index in the left segment
    return high

def quickselect(list, start_index, end_index, k):
    if start_index >= end_index:
        return list[start_index]

    low_last_index = partition(list, start_index, end_index)
    if k <= low_last_index:
        return quickselect(list, start_index, low_last_index, k)

    return quickselect(list, low_last_index + 1, end_index, k)


'''
    Unit Tests
    ----------
'''

list = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', list)
num = quickselect(list, 0, len(list) - 1, 1)
print('Number:', num)
print('SORTED:', list)

list = [151, 3002, 482, 5, 0, 84, -1, 8512, 8]
print('UNSORTED:', list)
num = quickselect(list, 0, len(list) - 1, 8)
print('Number:', num)
print('SORTED:', list)

list = [7, 86, 102, 4, -6, 806, 302, 1, 9, 25]
print('UNSORTED:', list)
num = quickselect(list, 0, len(list) - 1, 6)
print('Number:', num)
print('SORTED:', list)

list = [47, 81, 13, 5, 38, 96, 51, 64]
print('UNSORTED:', list)
num = quickselect(list, 0, len(list) - 1, 3)
print('Number:', num)
print('SORTED:', list)
