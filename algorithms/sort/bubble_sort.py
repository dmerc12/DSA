'''
    Bubble Sort Algorithm
    --------------------------------------------------------------------
    List must be integers

    Iterates through a list, comparing and swapping adjacent elements if the second element is less than the first

    Uses nested loops.

    Often considered impractical for real-world use since many faster sorting algorithms exist


    Time Complexity: Quadratic
    Time Complexity Notation: O(N^2)

    Space Complexity: Constant
    Space Complexity Notation: O(N)
    -------------------------------
'''

def bubble_sort(list):
    list_size = len(list)
    for i in range(list_size - 1):
        for j in range(list_size - i - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp

'''
    Unit Tests
    ----------
'''

list = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', list)
bubble_sort(list)
print('SORTED:', list)

list = [151, 3002, 482, 5, 0, 84, -1, 8512, 8]
print('UNSORTED:', list)
bubble_sort(list)
print('SORTED:', list)

list = [7, 86, 102, 4, -6, 806, 302, 1, 9, 25]
print('UNSORTED:', list)
bubble_sort(list)
print('SORTED:', list)

list = [47, 81, 13, 5, 38, 96, 51, 64]
print('UNSORTED:', list)
bubble_sort(list)
print('SORTED:', list)
