'''
    Linear Search Algorithm
    --------------------------------------------------------------------
    Returns the index position of the target if found, else returns None
    complexity: O(N)
'''
def linear_search(list, target):
    print('Target: ', target)
    for index in range(0, len(list)):
        if list[index] == target:
            return index
    else:
        return None

def verify(index):
    if index is not None:
        print('Target found at index: ', index)
    else:
        print('Target not found in the list')

numbers = [1,2,3,4,5,6,7,8,9,10]
print('List: ', numbers)

# Test if number is not in the list
result = linear_search(numbers, 12)
verify(result)

# Test if number is in the middle of the list
result = linear_search(numbers, 6)
verify(result)

# Test if number is in the front of the list
result = linear_search(numbers, 1)
verify(result)

# Test if number is in the back of the list
result = linear_search(numbers, 10)
verify(result)
