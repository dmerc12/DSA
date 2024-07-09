'''
    Stack
    -----
    Stack below can be bounded or unbounded using the optional parameter
'''

class Stack:

    # Initializes the stack. If the optional_max_length argument is  omitted or negative, the stack is unbounded. If the optional_max_length is non-negative, the stack is bounded.
    def __init__(self, optional_max_length = -1):
        self.stack_list = []
        self.max_length = optional_max_length

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
