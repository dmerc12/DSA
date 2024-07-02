'''
    Selection Sort Algorithm
    --------------------------------------------------------------------
    List does not have to be sorted for algorithm to work

    Sorts a list input as 2 parts, sorted and unsorted, and repeatedly selects the proper next value from unsorted part

    The index variable i denotes the dividing point. Elements to the left of i are sorted, and elements including and to the right of i are unsorted
    All elements in the unsorted part are searched to find the index of the element with the smallest value
    The variable index_smallest stores the index of the smallest element in the unsorted part
    Once the element with the smallest value is found, the element is swapped with the element at location i
    Then, the index i is advanced one place to the right, and the process repeats

    The term "selection" comes from the fact that for each iteration of the outer loop, a value is selected for position i

    Time Complexity: Linear
    Time Complexity Notation: O(N^2)

    Space Complexity: Constant
    Space Complexity Notation: O(N)
    -------------------------------
'''
def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
        # Swap numbers[i] and numbers[index_smallest]
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp

'''
    Unit Tests
    ----------
'''

list = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', list)
selection_sort(list)
print('SORTED:', list)

list = [151, 3002, 482, 5, 0, 84, -1, 8512, 8]
print('UNSORTED:', list)
selection_sort(list)
print('SORTED:', list)

list = ['k', 'g', 't', 'a', 'u', 'z', 'd', 'y']
print('UNSORTED:', list)
selection_sort(list)
print('SORTED:', list)

list = ['test', 'another', 'user', 'request']
print('UNSORTED:', list)
selection_sort(list)
print('SORTED:', list)
