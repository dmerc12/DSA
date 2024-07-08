'''
    Doubly-Linked List
    -------------------
'''

class Node:

    def __init__(self, initial_data):
        self.data = initial_data
        self.next: Node = None
        self.prev: Node = None

class DoublyLinkedList:

    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def append(self, new_node: Node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, new_node: Node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, current_node: Node, new_node: Node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            successor_node = current_node.next
            new_node.next = successor_node
            new_node.prev = current_node
            current_node.next = new_node
            successor_node.prev = new_node

    def remove(self, current_node: Node):
        successor_node = current_node.next
        predecessor_node = current_node.prev

        if successor_node is not None:
            successor_node.prev = predecessor_node

        if predecessor_node is not None:
            predecessor_node.next = successor_node

        if current_node is self.head:
            self.head = successor_node

        if current_node is self.tail:
            self.tail = predecessor_node

    def insertion_sort(self):
        current_node = self.head.next
        while current_node != None:
            next_node = current_node.next
            search_node = current_node.prev
            while ((search_node != None) and (search_node.data > current_node.data)):
                search_node = search_node.prev
            # Remove and re-insert curNode
            self.remove(current_node)
            if search_node == None:
                current_node.prev = None
                self.prepend(current_node)
            else:
                self.insert_after(search_node, current_node)
            # Advance to next node
            current_node = next_node
