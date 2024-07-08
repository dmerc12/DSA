'''
    Circular Linked List
    -------------------
    Can be singly or doubly linked list, example here uses a doubly linked list
'''

class Node:

    def __init__(self, initial_data):
        self.data = initial_data
        self.next: Node = None
        self.prev: Node = None

class CircularLinkedList:

    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def append(self, new_node: Node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.tail
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node

    def prepend(self, new_node: Node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.tail
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head = new_node

    def insert_after(self, current_node: Node, new_node: Node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.tail
        elif current_node is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        else:
            successor_node = current_node.next
            new_node.next = successor_node
            new_node.prev = current_node
            current_node.next = new_node
            successor_node.prev = new_node

    def remove(self, current_node: Node):
        if self.head is None:
            return

        if (self.head == self.tail) and (self.head == current_node):
            self.head = None
            self.tail = None
        elif self.head == current_node:
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
        elif self.tail == current_node:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        else:
            predecessor_node = current_node.prev
            successor_node = current_node.next
            predecessor_node.next = successor_node
            successor_node.prev = predecessor_node
