'''
    Binary Search Algorithm
    --------------------------------------------------------------------
    List must be sorted for algorithm to work

    Returns the index position of the target if found, else returns None

    Time Complexity: Logarithmic
    Time Complexity Notation: O(log N)

    Space Complexity: Constant
    Space Complexity Notation: O(1)
    -------------------------------
'''
def binary_search(list, target):
    print('Target: ', target)
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] < target:
            first = midpoint + 1
        elif list[midpoint] > target:
            last = midpoint - 1
        else:
            return midpoint
    return None

'''
    Unit Tests
    ----------
'''

def verify(index):
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target not found in the list')

numbers = [1,2,3,4,5,6,7,8,9,10]
print('List: ', numbers)

# Test if number is not in the list
target = 12
print('Target: ', target)
result = binary_search(numbers, target)
verify(result)

# Test if number is in the middle of the list
target = 6
print('Target: ', target)
result = binary_search(numbers, target)
verify(result)

# Test if number is in the front of the list
target = 1
print('Target: ', target)
result = binary_search(numbers, target)
verify(result)

# Test if number is in the back of the list
target = 10
print('Target: ', target)
result = binary_search(numbers, target)
verify(result)
