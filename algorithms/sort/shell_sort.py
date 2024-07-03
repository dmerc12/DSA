'''
    Shell Sort Algorithm
    --------------------------------------------------------------------
    Uses a variation of the insertion sort algorithm to sort subsets of an input list
    Instead of comparing elements that are immediately adjacent  to each other, the insesrtion sort variant compares elements that are at a fixed distance apart, known as a gap space
    Repeats this variation of insertion sort using different gap sizes and starting points within the input list

    Final gap value must be 1, the equivalent of a regular insertion sort

    Time Complexity: Sublinear / Subquadradic
    Time Complexity Notation: O(N^1.5)

    Space Complexity: Constant
    Space Complexity Notation: O(1)
    -------------------------------
'''

def insertion_sort_interleaved(list, start_index, gap):
    for i in range(start_index + gap, len(list),  gap):
        j = i
        while (j - gap >= start_index) and (list[j] < list[j - gap]):
            temp = list[j]
            list[j] = list[j - gap]
            list[j - gap] = temp
            j = j - gap

def shell_sort(list, gap_values):
    for gap_value in gap_values:
        for i in range(gap_value):
            insertion_sort_interleaved(list, i, gap_value)

'''
    Unit Tests
    ----------
'''

list = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', list)
shell_sort(list, [4, 2, 1])
print('SORTED:', list)

list = [151, 3002, 482, 5, 0, 84, -1, 8512, 8]
print('UNSORTED:', list)
shell_sort(list, [4, 2, 1])
print('SORTED:', list)

list = ['k', 'g', 't', 'a', 'u', 'z', 'd', 'y']
print('UNSORTED:', list)
shell_sort(list, [4, 2, 1])
print('SORTED:', list)

list = ['test', 'another', 'user', 'request']
print('UNSORTED:', list)
shell_sort(list, [2, 1])
print('SORTED:', list)
