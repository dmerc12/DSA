'''
    Radix Sort Algorithm
    --------------------------------------------------------------------
    List must be integers
    A type of bucket sort

    Algorithm goes one digit at a time starting with the least significant digit and ending with the most significant
    Two steps are needed with each digit:
    1. All array elements are placed into buckets based on the current digit's value
    2. The array is rebuilt by removing all elements from buckets, in order from lowest bucket to highest

    Time Complexity:
    Time Complexity Notation:

    Space Complexity:
    Space Complexity Notation:
    -------------------------------
'''

# Returns the maximum length, in number of digits, out of all list elements
def radix_get_max_length(list):
    max_digits = 0
    for num in list:
        digit_count = radix_get_length(num)
        if digit_count > max_digits:
            max_digits = digit_count
    return max_digits

# Returns the length, in number of digits, of value
def radix_get_length(value):
    if value == 0:
        return 1

    digits = 0
    while value != 0:
        digits += 1
        value = int(value / 10)
    return digits

def radix_sort(list):
    buckets = []
    for i in range(10):
        buckets.append([])

    # Find the max length, in number of digits
    max_digits = radix_get_max_length(list)

    pow_10 = 1
    for digit_index in range(max_digits):
        for num in list:
            bucket_index = (abs(num) // pow_10) % 10
            buckets[bucket_index].append(num)

        list.clear()
        for bucket in buckets:
            list.extend(bucket)
            bucket.clear()

        pow_10 = pow_10 * 10

    negatives = []
    non_negatives = []
    for num in list:
        if num < 0:
            negatives.append(num)
        else:
            non_negatives.append(num)
    negatives.reverse()
    list.clear()
    list.extend(negatives + non_negatives)

'''
    Unit Tests
    ----------
'''

list = [10, 2, 78, 4, 45, 32, 7, 11]
print('UNSORTED:', list)
radix_sort(list)
print('SORTED:', list)

list = [151, 3002, 482, 5, 0, 84, -1, 8512, 8]
print('UNSORTED:', list)
radix_sort(list)
print('SORTED:', list)

list = [7, 86, 102, 4, -6, 806, 302, 1, 9, 25]
print('UNSORTED:', list)
radix_sort(list)
print('SORTED:', list)

list = [47, 81, 13, 5, 38, 96, 51, 64]
print('UNSORTED:', list)
radix_sort(list)
print('SORTED:', list)
