'''
    Recursive Binary Search Algorithm
    --------------------------------------------------------------------
    List must be sorted for algorithm to work

    Returns the index position of the target if found, else returns None

    RECURSIVE DEPTH: The number of times the recursive function calls itself

    Time Complexity: Logarithmic
    Time Complexity Notation: O(log N)
    ----------------------------------
'''
def recursive_binary_search(list, target, start=0):
    if len(list) == 0:
        return None
    else:
        midpoint = (len(list)) // 2
        if list[midpoint] == target:
            return start + midpoint
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target, start + midpoint + 1)
            else:
                return recursive_binary_search(list[:midpoint - 1], target, start)

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
result = recursive_binary_search(numbers, target)
verify(result)

# Test if number is in the middle of the list
target = 6
print('Target: ', target)
result = recursive_binary_search(numbers, target)
verify(result)

# Test if number is in the front of the list
target = 1
print('Target: ', target)
result = recursive_binary_search(numbers, target)
verify(result)

# Test if number is in the back of the list
target = 10
print('Target: ', target)
result = recursive_binary_search(numbers, target)
verify(result)
