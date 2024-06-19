'''
    Linear Search Algorithm
    --------------------------------------------------------------------
    List does not have to be sorted for algorithm to work

    Returns the index position of the target if found, else returns None

    Time Complexity: Linear
    Time Complexity Notation: O(N)

    Space Complexity: Constant
    Space Complexity Notation: O(1)
    -------------------------------
'''
def linear_search(list, target):
    print('Target: ', target)
    for index in range(0, len(list)):
        if list[index] == target:
            return index
    else:
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
result = linear_search(numbers, target)
verify(result)

# Test if number is in the middle of the list
target = 6
print('Target: ', target)
result = linear_search(numbers, target)
verify(result)

# Test if number is in the front of the list
target = 1
print('Target: ', target)
result = linear_search(numbers, target)
verify(result)

# Test if number is in the back of the list
target = 10
print('Target: ', target)
result = linear_search(numbers, target)
verify(result)
