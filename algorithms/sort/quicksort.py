'''
    Quicksort Algorithm
    --------------------------------------------------------------------
    Repeatedly partitions the input into unsorted low and high parts using a pivot value, then recursively sorts each of those parts.

    Time Complexity: Log Linear or Quadradic
    Time Complexity Notation: O(N log N) or O(N^2)

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



def quicksort(list, start_index, end_index):
    # Only attempt to sort the list segment if there are atleast 2 elements
    if end_index <= start_index:
        return

    # Partition the list segment
    high = partition(list, start_index, end_index)

    # Recursively sort the left segment
    quicksort(list, start_index, high)

    # Recursively sort the right segment
    quicksort(list, high + 1, end_index)

'''
    Unit Tests
    ----------
'''

list = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', list)
quicksort(list, 0, len(list) - 1)
print('SORTED:', list)

list = [151, 3002, 482, 5, 0, 84, -1, 8512, 8]
print('UNSORTED:', list)
quicksort(list, 0, len(list) - 1)
print('SORTED:', list)

list = ['k', 'g', 't', 'a', 'u', 'z', 'd', 'y']
print('UNSORTED:', list)
quicksort(list, 0, len(list) - 1)
print('SORTED:', list)

list = ['test', 'another', 'user', 'request']
print('UNSORTED:', list)
quicksort(list, 0, len(list) - 1)
print('SORTED:', list)
