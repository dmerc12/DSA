'''
    Binary Search Algorithm
    --------------------------------------------------------------------
    List must be sorted for algorithm to work

    Returns the index position of the target if found, else returns None
    
    complexity: O(log N)
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

def verify(index):
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target not found in the list')

numbers = [1,2,3,4,5,6,7,8,9,10]
print('List: ', numbers)

# Test if number is not in the list
result = binary_search(numbers, 12)
verify(result)

# Test if number is in the middle of the list
result = binary_search(numbers, 6)
verify(result)

# Test if number is in the front of the list
result = binary_search(numbers, 1)
verify(result)

# Test if number is in the back of the list
result = binary_search(numbers, 10)
verify(result)
