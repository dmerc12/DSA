from node import Node

'''
    Singly-Linked List
    -------------------
'''

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

    def remove_after(self, current_node: Node | None):
        if (current_node is None) and (self.head is not None):
            succeeding_node = self.head.next
            self.head = succeeding_node
            if succeeding_node is None:
                self.tail = None
        elif current_node.next is not None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node == None:
                self.tail = current_node

    def insertion_sort(self):
        before_current = self.head
        current_node = self.head.next
        while current_node != None:
            next_node = current_node.next
            position = self.find_insertion_position(current_node.data)
            if position == before_current:
                before_current = current_node
            else:
                # Remove and re-insert curNode
                self.remove_after(before_current)
                if position == None:
                    self.prepend(current_node)
                else:
                    self.insert_after(position, current_node)
            # Advance to next node
            current_node = next_node

    def find_insertion_position(self, data_value):
        position_a = None
        position_b = self.head
        while (position_b != None) and (data_value > position_b.data):
            position_a = position_b
            position_b = position_b.next
        return position_a

'''
    Doubly-Linked List
    -------------------
'''

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

'''
    Circular Linked List
    -------------------
    Can be singly or doubly linked list, example here uses a doubly linked list
'''

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
