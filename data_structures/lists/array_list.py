'''
   Array-Based List
    -------------------
'''

class ArrayList:

    def __init__(self, initial_allocation_size = 10):
        self.allocation_size = initial_allocation_size
        self.length = 0
        self.array = [None] * initial_allocation_size

    def resize(self, new_allocation_size):
        # create a new array with the indicated size
        new_array = [None] * new_allocation_size
        # copy items in current array into the new array
        for i in range(self.length):
            new_array[i] = self.array[i]
        # assign the array data member with the new array
        self.array = new_array
        # update the allocation size
        self.allocation_size = new_allocation_size

    def append(self, new_item):
        # resize if the array is full
        if self.allocation_size == self.length:
            self.resize(self.length * 2)
        # insert the new item at index equal to self.length
        self.array[self.length] = new_item
        # increment the array's length
        self.length = self.length + 1

    def prepend(self, new_item):
        # resize if the array is full
        if self.allocation_size == self.length:
            self.resize(self.length * 2)
        # shift all array items to the right, starting from the last index and moving down to the first index
        for i in reversed(range(1, self.length + 1)):
            self.array[i] = self.array[i - 1]
        # insert the new item at index 0
        self.array[0] = new_item
        # update the array's length
        self.length = self.length + 1

    def insert_after(self, index, new_item):
        # resize if the array is full
        if self.allocation_size == self.length:
            self.resize(self.length * 2)
        # shift all array items to the right, starting from the last index and moving down to the index just past the given index
        for i in reversed(range(index + 1, self.length + 1)):
            self.array[i] = self.array[i - 1]
        # insert the new item at the index just past the given index
        self.array[index + 1] = new_item
        # update the array's length
        self.length = self.length + 1

    def search(self, item):
        # iterate through the entire array
        for i in range(self.length):
            # if the current item matches the search item, return the current index immediately
            if self.array[i] == item:
                return i
        # if the above loop finishes without returning, it means the search item was not found
        return -1

    def remove_at(self, index):
        # make sure the index is valid for the current array
        if index >= 0 and index < self.length:
            # shift items from the given index up to the end of the array
            for i in range(index, self.length - 1):
                self.array[i] = self.array[i + 1]
            # update the array's length
            self.length = self.length - 1
