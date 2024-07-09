'''
    Linked List Node
    ----------------
    Use only self.next for singly linked list, and both for doubly linked list
'''

class Node:

    def __init__(self, initial_data):
        self.data = initial_data
        self.next: Node = None
        self.prev: Node = None
