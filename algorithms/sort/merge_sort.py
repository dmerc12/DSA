'''
    Merge Algorithm
    --------------------------------------------------------------------
    Divides a list into two halves, recursively sorts each half, then merges the sorted halvess to produce a sorted list
    Recursive partitioning continues until a list of one element is reached
    Merges the two sorted partitions into a single list by repeatedly selecting the smallest element from either the left or right partition and adding that element to a temporary merged list
    Once fully merged, the elements in the temporary merged list are copied back to the original list

    Time Complexity: Log Linear
    Time Complexity Notation: O(N log N)

    Space Complexity: Linear
    Space Complexity Notation: O(N)
    -------------------------------
'''

def merge(list, i, j, k):
    merged_size = k - i + 1         # Size of merged partition
    merged_list = [0] * merged_size # Dynamically allocates temporary array for merged list

    merge_pos = 0     # Position to insert merged index
    left_pos = i      # Initialize left partition position
    right_pos = j + 1 # Initialize right partition position

    # Add smallest elements from left or right partition to merged list
    while left_pos <= j and right_pos <= k:
        if list[left_pos] <= list[right_pos]:
            merged_list[merge_pos] = list[left_pos]
            left_pos += 1
        else:
            merged_list[merge_pos] = list[right_pos]
            right_pos += 1
        merge_pos = merge_pos + 1

    # If left partition is not empty, add remaining elements to merged list
    while left_pos <= j:
        merged_list[merge_pos] = list[left_pos]
        left_pos += 1
        merge_pos += 1

    # If right partition is not empty, add remaining elements to merged numbers
    while right_pos <= k:
        merged_list[merge_pos] = list[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    # Copy merge item back to list
    for merge_pos in range(merged_size):
        list[i + merge_pos] = merged_list[merge_pos]

def merge_sort(list, i, k):
    j = 0

    if i < k:
        # Find the midpoint in the partition
        j = (i + k) // 2

        # Recursively sort left and right partitions
        merge_sort(list, i, j)
        merge_sort(list, j + 1, k)

        # Merge left and right partition in sorted order
        merge(list, i, j, k)

'''
    Unit Tests
    ----------
'''

list = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', list)
merge_sort(list, 0, len(list) - 1)
print('SORTED:', list)

list = [151, 3002, 482, 5, 0, 84, -1, 8512, 8]
print('UNSORTED:', list)
merge_sort(list, 0, len(list) - 1)
print('SORTED:', list)

list = ['k', 'g', 't', 'a', 'u', 'z', 'd', 'y']
print('UNSORTED:', list)
merge_sort(list, 0, len(list) - 1)
print('SORTED:', list)

list = ['test', 'another', 'user', 'request']
print('UNSORTED:', list)
merge_sort(list, 0, len(list) - 1)
print('SORTED:', list)
