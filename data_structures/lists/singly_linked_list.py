'''
    Singly-Linked List
    -------------------
'''

class Node:

    def __init__(self, initial_data):
        self.data = initial_data
        self.next: Node = None

class SinglyLinkedList:

    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def append(self, new_node: Node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, new_node: Node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node: Node, new_node: Node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def remove_after(self, current_node: Node):
        if (current_node == None) and (self.head != None):
            succeeding_node = self.head.next
            self.head = succeeding_node
            if succeeding_node == None:
                self.tail = None
        elif current_node.next != None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node == None:
                self.tail = current_node
