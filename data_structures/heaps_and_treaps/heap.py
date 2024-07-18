'''
    Max Heap
    --------
'''
class MaxHeap:
    def __init__(self):
        self.heap_array = []

    def percolate_up(self, node_index):
        while node_index > 0:
            # Compute the parent node's index.
            parent_index = (node_index - 1) // 2
            # Check for a violation of the max heap property.
            if self.heap_array[node_index] <= self.heap_array[parent_index]:
                # No violation, so percolate up is done.
                return
            else:
                # Swap heap_array[node_index] and heap_array[parent_index].
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[parent_index]
                self.heap_array[parent_index] = temp
                # Continue the loop from the parent node.
                node_index = parent_index

    def percolate_down(self, node_index):
        child_index = 2 * node_index + 1
        value = self.heap_array[node_index]
        while child_index < len(self.heap_array):
            # Find the max among the node and the node's children.
            max_value = value
            max_index = -1
            i = 0
            while i < 2 and i + child_index < len(self.heap_array):
                if self.heap_array[i + child_index] > max_value:
                    max_value = self.heap_array[i + child_index]
                    max_index = i + child_index
                i = i + 1
            # Check for a violation of the max heap property.
            if max_value == value:
                return
            else:
                # Swap heap_array[node_index] and heap_index[max_index].
                temp = self.heap_array[node_index]
                self.heap_array[node_index] = self.heap_array[max_index]
                self.heap_array[max_index] = temp
                # Continue loopp from the larger child node.
                node_index = max_index
                child_index = 2 * node_index + 1

    def insert(self, value):
        # Add the new value to the end of the array.
        self.heap_array.append(value)
        # Percolate up from the last index to restore heap property.
        self.percolate_up(len(self.heap_array) - 1)

    def remove(self):
        # Save the max value from the root of  the heap.
        max_value = self.heap_array[0]
        # Move the last item in the array into index 0.
        replace_value = self.heap_array.pop()
        if len(self.heap_array) > 0:
            self.heap_array[0] = replace_value
            # Percolate down to restore max heap property.
            self.percolate_down(0)
        return max_value

    # Binary max heap percolate down.
    def max_heap_percolate_down(node_index, heap_list, list_size):
        child_index = 2 * node_index + 1
        value = heap_list[node_index]
        while child_index < list_size:
            # Find the max amng the node and all the node's childrern.
            max_value = value
            max_index = -1
            i = 0
            while i < 2 and i + child_index < list_size:
                if heap_list[i + child_index] > max_value:
                    max_value = heap_list[i + child_index]
                    max_index = i + child_index
                i = i + 1
            if max_value == value:
                return
            # Swap heap_list[node_index] and heap_list[max_index].
            temp = heap_list[node_index]
            heap_list[node_index] = heap_list[max_index]
            heap_list[max_index] = temp
            node_index = max_index
            child_index = 2 * node_index + 1

    # Sorts the list of numbers using the heap sort algorithm.
    def heap_sort(numbers):
        # Heapify numbers lists.
        i = len(numbers) // 2 - 1
        while i >= 0:
            MaxHeap.max_heap_percolate_down(i, numbers, len(numbers))
            i = i - 1
        i = len(numbers) - 1
        while i > 0:
            # Swap numbers [0] and numbers[i].
            temp = numbers[0]
            numbers[0] = numbers[i]
            numbers[i] = temp
            MaxHeap.max_heap_percolate_down(0, numbers, i)
            i = i - 1
