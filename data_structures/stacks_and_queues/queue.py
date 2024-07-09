'''
    Array-Based Queue
    -----------------
    Queue below can be bounded or unbounded using the optional parameter
'''

class ArrayQueue:

    # Initializes the queue. If the optional max_length argument is  omitted or negative, the queue is unbounded. If the optional max_length is non-negative, the queue is bounded.
    def __init__(self, max_length = -1):
        self.queue_list = [0]
        self.front_index = 0
        self.length = 0
        self.max_length = max_length

    def resize(self):
        # Create new list and copy existing items.
        new_size = len(self.queue_list) * 2
        if self.max_length >= 0 and new_size > self.max_length:
            new_size = self.max_length
        new_list = [0] * new_size
        for i in range(self.length):
            item_index = (self.front_index + i) % len(self.queue_list)
            new_list[i] = self.queue_list[item_index]
        # Assign new list and reset front index to 0.
        self.queue_list = new_list
        self.front_index = 0

    def enqueue(self, item):
        # If at max length, return false.
        if self.length == self.max_length:
            return False
        # Resize if length equals allocation size.
        if self.length == len(self.queue_list):
            self.resize()
        # Enqueue item
        item_index = (self.front_index + self.length) % len(self.queue_list)
        self.queue_list[item_index] = item
        self.length += 1
        return True

    def dequeue(self):
        # Get the item at front of queue.
        to_return = self.queue_list[self.front_index]
        # Decrement length and advance front index.
        self.length -= 1
        self.front_index = (self.front_index + 1) % len(self.queue_list)
        # Return front item.
        return to_return

'''
    Linked-List Queue
    -----------------
'''

from lists.linked_list import SinglyLinkedList
from lists.node import Node

class Queue:

    def __init__(self):
        self.list = SinglyLinkedList()

    def enqueue(self, new_item):
        # Create a new node to hold the item.
        new_node = Node(new_item)
        # Insert the node as the list tail (end of the queue).
        self.list.append(new_node)

    def dequeue(self):
        # Copy data from the list's head node (queue's top node).
        dequeued_item = self.list.head.data
        # Remove list head..
        self.list.remove_after(None)
        # Return dequeued item.
        return dequeued_item
