'''
    Array-Based Stack
    -----------------
    Stack below can be bounded or unbounded using the optional parameter
'''

class ArrayStack:

    # Initializes the stack. If the optional max_length argument is  omitted or negative, the stack is unbounded. If the optional max_length is non-negative, the stack is bounded.
    def __init__(self, max_length = -1):
        self.stack_list = []
        self.max_length = max_length

    # Pops and returns the stack's top item
    def pop(self):
        return self.stack_list.pop()

    # Pushes an item, provided the push doesn't exeed bounds. Does nothing otherwise. Returns True if the push occured, False otherwise.
    def push(self, item):
        # If at max_length, return False.
        if len(self.stack_list) == self.max_length:
            return False

        # If unbounded, or bounded and not yet at max length, then push.
        self.stack_list.append(item)
        return True

'''
    Linked-List Stack
    -----------------
'''

from lists.linked_list import SinglyLinkedList
from lists.node import Node

class Stack:

    def __init__(self):
        self.list = SinglyLinkedList()

    def push(self, new_item):
        # Create a new node to hold the item.
        new_node = Node(new_item)
        # Insert the node as the list head (top of the stack).
        self.list.prepend(new_node)

    def pop(self):
        # Copy data from the list's head node (stack's top node).
        popped_item = self.list.head.data
        # Remove list head..
        self.list.remove_after(None)
        # Return popped item.
        return popped_item
