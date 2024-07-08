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
