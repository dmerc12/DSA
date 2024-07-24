'''
    B-Tree (2-3-4 tree)
    -------------------
'''
class Tree234:
    # Node234 class - represents a node in a 2-3-4 tree.
    class Node234:
        def __init__(self, key_A, left_child = None, middle1_child = None):
            self.A = key_A
            self.B = None
            self.C = None
            self.left: Tree234.Node234 | None = left_child
            self.middle1: Tree234.Node234 | None = middle1_child
            self.middle2: Tree234.Node234 | None = None
            self.right: Tree234.Node234 | None = None

        # Returns the left, middle1, middle2, or right child if the child_index argument is 0, 1, 3, or 3, respectively.
        # Returns None if the child_index argument is < 0 or > 3.
        def get_child(self, child_index):
            if child_index == 0:
                return self.left
            elif child_index == 1:
                return self.middle1
            elif child_index == 2:
                return self.middle2
            elif child_index == 3:
                return self.right

        # Returns 0, 1, 2, or 3 if the child argument is this node's left, middle1, middle2, or right child, respectively.
        # Returns -1 if the child argument is not a child of this node.
        def get_child_index(self, child):
            if child is self.left:
                return 0
            elif child is self.middle1:
                return 1
            elif child is self.middle2:
                return 2
            elif child is self.right:
                return 3
            return -1

        # Returns this node's A, B, or C key, if the key_index argument is 0, 1, or 2, respectively.
        # Returns None if the key_index argument is < 0 or > 2.
        def get_key(self, key_index):
            if key_index == 0:
                return self.A
            elif key_index == 1:
                return self.B
            elif key_index == 2:
                return self.C
            return None

        # Returns 0, 1, or 2, if the key argument is this node's A, B, or C child, respectively.
        # Returns -1 if the key argument is not a key of this node.
        def get_key_index(self, key):
            if key == self.A:
                return 0
            elif key == self.B:
                return 1
            elif key == self.C:
                return 2
            return -1

        # Appends 1 key and 1 child to this node.
        # Preconditions:
        # 1. This node has 1 or 2 keys.
        # 2. key > all keyss in this node.
        # 3. Child subtree contains only keys > key.
        def append_key_and_child(self, key, child):
            if self.B == None:
                self.B = key
                self.middle2 = child
            else:
                self.C = key
                self.right = child

        # Returns the number of keys in this node, which will be 1, 2, or 3.
        def count_keys(self):
            if self.C != None:
                return 3
            elif self.B != None:
                return 2
            return 1

        # Returns True if this node has the specified key, False otherwise.
        def has_key(self, key):
            return self.A == key or self.B == key or self.C == key

        # Inserts a new key into the proper location in this node.
        # Precondition: This node is a leaf and has 2 or fewer keys.
        def insert_key(self, key):
            if key < self.A:
                self.C = self.B
                self.B = self.A
                self.A = key
            elif self.B == None or key < self.B:
                self.C = self.B
                self.B = key
            else:
                self.C = key

        # Inserts a new key into the proper location in this node, and sets the children on either side of the inserted key.
        # Precondition: This node has 2 or fewer keys.
        def insert_key_with_children(self, key, leftChild, rightChild):
            if key < self.A:
                self.C = self.B
                self.B = self.A
                self.A = key
                self.right = self.middle2
                self.middle2 = self.middle1
                self.middle1 = rightChild
                self.left = leftChild
            elif self.B == None or key < self.B:
                self.C = self.B
                self.B = key
                self.right = self.middle2
                self.middle2 = rightChild
                self.middle1 = leftChild
            else:
                self.C = key
                self.right = rightChild
                self.middle2 = leftChild

        # Returns True if this node is a leaf, False otherwise.
        def is_leaf(self):
            return self.left == None

        # Returns the child of this node that would be visited next in the traversal to search for the specified key.
        def next_node(self, key):
            if key < self.A:
                return self.left
            elif self.B == None or key < self.B:
                return self.middle1
            elif self.C == None or key < self.C:
                return self.middle2
            return self.right

        # Removes key A, B, or C from this node, if key_index is 0, 1, or 2, respectively.
        # Other keys and children are shifted as necessary.
        def remove_key(self, key_index):
            if key_index == 0:
                self.A = self.B
                self.B = self.C
                self.C =  None
                self.left = self.middle1
                self.middle1 = self.middle2
                self.middle2 = self.right
                self.right = None
            elif key_index == 1:
                self.B = self.C
                self.C = None
                self.middle2 = self.right
                self.right = None
            elif key_index == 2:
                self.C = None
                self.right = None

        # Removes and returns the rightmost child.
        # Two possible cases exist:
        # 1. If this node has a right child, right is set to None, and the previous right value is returned.
        # 2. Else if this node has a middle2 child, middle2 is set to None, and the previous right value is returned.
        # 3. Otherwise no action is taken and None is returned.
        # No keys are changed in any case.
        def remove_rightmost_child(self):
            removed = None
            if self.right != None:
                removed = self.right
                self.right = None
            elif self.middle2 != None:
                removed = self.middle2
                self.middle2 = None
            return removed

        # Removes and returns the rightmost key.
        # Three possible cases exist:
        # 1. If this node has 3 keys, C is set to None and the previous C value is returned.
        # 2. If this node has 2 keys, B is set to None and the previous B value is returned.
        # 3. Otherwise no action is taken and None is returned.
        # No children are changed in any case.
        def remove_rightmost_key(self):
            removed = None
            if self.C != None:
                removed = self.C
                self.C = None
            elif self.B != None:
                removed = self.B
                self.B = None
            return removed

        # Sets the left, middle1, middle2, or right child if the child_index argument is 0, 1, 2, or 3 respectively.
        # Does nothing if the child_index argument is < 0 or > 3.
        def set_child(self, child, child_index):
            if child_index == 0:
                self.left = child
            elif child_index == 1:
                self.middle1 = child
            elif child_index == 2:
                self.middle2 = child
            elif child_index == 3:
                self.right = child

        # Sets this node's A, B, or C key if the key_index argument is 0, 1, or 2, respectively.
        # Does nothing if the key_index argument is < 0 or > 2.
        def set_key(self, key, key_index):
            if key_index == 0:
                self.A = key
            elif key_index == 1:
                self.B = key
            elif key_index == 2:
                self.C = key

    # Initializes the tree with the root node reference set to None.
    def __init__(self):
        self.root: Tree234.Node234 | None = None

    # Inserts a new key into this tree, provided the tree doesn't already contain the same key.
    def insert(self, key, node: 'Tree234.Node234' | None = None, node_parent: 'Tree234.Node234' | None = None):
        # Special case for empty tree.
        if self.root == None:
            self.root = Tree234.Node234(key)
            return self.root
        # If the node argument is null, recursively call with root.
        if node == None:
            return self.insert(key, self.root, None)
        # Check for duplicate key.
        if node.has_key(key):
            # Duplicate keys are not allowed.
            return None
        # Preemptiveely split full nodes.
        if node.C != None:
            node = self.split(node, node_parent)
        if not node.is_leaf():
            if key < node.A:
                return self.insert(key, node.left, node)
            elif node.B == None or key < node.B:
                return self.insert(key, node.middle1, node)
            elif node.C == None or key < node.C:
                return self.insert(key, node.middle2, node)
            else:
                return self.insert(key, node.right, node)
        # Key can be inserted into leaf node
        node.insert_key(key)
        return node

    # Searches this tree for the specified key.
    # If found, the node containing the key is returned.
    # Otherwise None is returned.
    def search(self, key):
        return self.search_recursive(key, self.root)

    # Recursive helper method for search.
    def search_recursive(self, key, node: 'Tree234.Node234' | None):
        if node == None:
            return None
        # Check if  the node contains the key.
        if node.has_key(key):
            return node
        # Recursively search the appropriate subtree.
        if key < node.A:
            return self.search_recursive(key, node.left)
        elif node.B == None or key < node.B:
            return self.search_recursive(key, node.middle1)
        elif node.C == None or key < node.C:
            return self.search_recursive(key, node.middle2)
        return self.search_recursive(key, node.right)

    # Splits a full node, moving the middle key up into the parent node.
    def split(self, node: 'Tree234.Node234' | None, node_parent: 'Tree234.Node234' | None):
        split_left = Tree234.Node234(node.A, node.left, node.middle1)
        split_right = Tree234.Node234(node.C, node.middle2, node.right)
        if node_parent is not None:
            node_parent.insert_key_with_children(node.B, split_left, split_right)
        else:
            # Split root.
            node_parent = Tree234.Node234(node.B, split_left, split_right)
            self.root = node_parent
        return node_parent

    # Fuses a parent node and two children into one node.
    # Precondition: Each of the three nodes must have one key each.
    def fuse(self, parent: 'Tree234.Node234', left_node: 'Tree234.Node234', right_node: 'Tree234.Node234'):
        if parent is self.root and parent.count_keys() == 1:
            return self.fuse_root()
        left_node_index = parent.get_child_index(left_node)
        middle_key = parent.get_key(left_node_index)
        fused_node = Tree234.Node234(left_node.A)
        fused_node.B = middle_key
        fused_node.C = right_node.A
        fused_node.left = left_node.left
        fused_node.middle1 = left_node.middle1
        fused_node.middle2 = right_node.left
        fused_node.right = right_node.middle1
        key_index = parent.get_key_index(middle_key)
        parent.remove_key(key_index)
        parent.set_child(fused_node, key_index)
        return fused_node

    # Fuses the tree's root node with the root's two children.
    # Precondition: Each of the three nodes must have one key each.
    def fuse_root(self):
        old_left = self.root.left
        old_middle1 = self.root.middle1
        self.root.B = self.root.A
        self.root.A = old_left.A
        self.root.C = old_middle1.A
        self.root.left = old_left.left
        self.root.middle1 = old_left.middle1
        self.root.middle2 = old_middle1.left
        self.root.right = old_middle1.middle1
        return self.root

    # Searches for, and returns, the minimum key in a subtree.
    def get_min_key(self, node: 'Tree234.Node234'):
        current = node
        while current.left != None:
            current = current.left
        return current.A

    # Finds and replaces one key with another.
    # The replacement key must be known to be a key that can be used as a replacement without violating any of the 2-3-4 tree rules.
    def key_swap(self, node: 'Tree234.Node234' | None, existing, replacement):
        if node == None:
            return False
        key_index = node.get_key_index(existing)
        if key_index == -1:
            next = node.next_node(existing)
            return self.key_swap(next, existing, replacement)
        if key_index == 0:
            node.A = replacement
        elif key_index == 1:
            node.B = replacement
        else:
            node.C = replacement
        return True

    # Rotates or fuses to add 1 or 2 additional keys to a node with 1 key.
    def merge(self, node: 'Tree234.Node234', node_parent: 'Tree234.Node234'):
        # Get references to node's siblings.
        node_index = node_parent.get_child_index(node)
        left_sibling = node_parent.get_child(node_index - 1)
        right_sibling = node_parent.get_child(node_index + 1)
        # Check siblings for a key that can be transferred.
        if left_sibling != None and left_sibling.count_keys() >= 2:
            self.rotate_right(left_sibling, node_parent)
        elif right_sibling != None and right_sibling.count_keys() >=2:
            self.rotate_left(right_sibling, node_parent)
        # False.
        else:
            if left_sibling == None:
                node = self.fuse(node_parent, node, right_sibling)
            else:
                node = self.fuse(node_parent, left_sibling, node)
        return node

    # Finds and removes the specified key from this tree.
    def remove(self, key):
        # Special case for tree with 1 key.
        if self.root.is_leaf() and self.root.count_keys() == 1:
            if self.root.A == key:
                self.root = None
                return True
            return False
        current_parent = None
        current = self.root
        while current != None:
            # Merge any non-root node with 1 key.
            if current.count_keys() == 1 and current is not self.root:
                current = self.merge(current, current_parent)
            # Check if current node contains key.
            key_index = current.get_key_index(key)
            if key_index != -1:
                if current.is_leaf():
                    current.remove_key(key_index)
                    return True
                # The node contains the key and is not a leaf, so the key is replaced with the successor.
                tmp_child = current.get_child(key_index + 1)
                tmp_key = self.get_min_key(tmp_child)
                self.remove(tmp_key)
                self.key_swap(self.root, key, tmp_key)
                return True
            # Current node does not contain key, so continue down tree.
            current_parent = current
            current = current.next_node(key)
        # Key not found.
        return False

    def rotate_left(self, node: 'Tree234.Node234', node_parent: 'Tree234.Node234'):
        # Get the node's left sibling.
        node_index = node_parent.get_child_index(node)
        left_sibling = node_parent.get_child(node_index - 1)
        # Get the key from the parent that will be copied into the left sibling.
        key_for_left_sibling = node_parent.get_key(node_index - 1)
        # Append the key to the left sibling.
        left_sibling.append_key_and_child(key_for_left_sibling, node.left)
        # Replace the parent's key that was appended to the left sibling.
        node_parent.set_key(node.A, node_index - 1)
        # Remove key A and left child from node.
        node.remove_key(0)

    def rotate_right(self, node: 'Tree234.Node234', node_parent: 'Tree234.Node234'):
        # Get the node's right sibling.
        node_index = node_parent.get_child_index(node)
        right_sibling = node_parent.get_child(node_index + 1)
        # Get the key from the parent that will be copied into the right sibling.
        key_for_right_sibling = node_parent.get_key(node_index)
        # Shift key and child references in right sibling.
        right_sibling.C = right_sibling.B
        right_sibling.B = right_sibling.A
        right_sibling.right = right_sibling.middle2
        right_sibling.middle2 = right_sibling.middle1
        right_sibling.middle1 = right_sibling.left
        # Set key A and the left child of right_sibling.
        right_sibling.A = key_for_right_sibling
        right_sibling.left = node.remove_rightmost_child()
        # Replace the parent's key that was prepended to the right sibling.
        node_parent.set_key(node.remove_rightmost_key(), node_index)
