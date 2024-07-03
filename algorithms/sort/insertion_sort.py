'''
    Insertion Sort Algorithm
    --------------------------------------------------------------------
    Sorts a list input as 2 parts, sorted and unsorted, and inserts the next value from the unsorted part into the correct location in the sorted part

    The index variable i denotes the starting position of the current element in the unsorted part
    Initially, the first element is assumed to be sorted, so the outer loop initializes to 1
    The inner while loop inserts the current element into the sorted part by repeatedly swapping the current element with the elements in the sorted part
    Once a smaller or equal element is found in the sorted part, the current element has been inserted in the correct location and the while loop terminates

    Time Complexity: Quadradic
    Time Complexity Notation: O(N^2)

    Space Complexity: Constant
    Space Complexity Notation: O(1)
    -------------------------------
'''

def insertion_sort(list):
    for i in range(1, len(list)):
        j = i
        # Insert list[i] into sorted part
        # Stopping once list[i] in correct position
        while j > 0 and list[j] < list[j - 1]:
            # Swap list[j] and listp[j - 1]
            temp = list[j]
            list[j] = list[j - 1]
            list[j - 1] = temp
            j = j - 1

'''
    Unit Tests
    ----------
'''

list = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', list)
insertion_sort(list)
print('SORTED:', list)

list = [151, 3002, 482, 5, 0, 84, -1, 8512, 8]
print('UNSORTED:', list)
insertion_sort(list)
print('SORTED:', list)

list = ['k', 'g', 't', 'a', 'u', 'z', 'd', 'y']
print('UNSORTED:', list)
insertion_sort(list)
print('SORTED:', list)

list = ['test', 'another', 'user', 'request']
print('UNSORTED:', list)
insertion_sort(list)
print('SORTED:', list)
