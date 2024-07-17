'''
    Binary Search Tree
    ------------------
'''
class BinarySearchTree:
    class BSTNode:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def search(self, desired_key):
        current_node = self.root
        while current_node is not None:
            # Return the node if the key matches.
            if current_node.key == desired_key:
                return current_node
            # Navigate to the left if the search key is less than the node's key.
            elif desired_key < current_node.key:
                current_node = current_node.left
            # Navigate to the right if the search key is greater than the node's key.
            else:
                current_node = current_node.right
        # The key was not found in the tree.
        return None

    def insert(self, node: BSTNode):
        # Check if the tree is empty.
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if node.key < current_node.key:
                    # If there is no left child, add the new node here.
                    # Otherwise repeat from the left child.
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    # If there is no right child, add the new node here.
                    # Otherwise repeat from the right child.
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right

    def remove(self, key):
        parent = None
        current_node = self.root
        # Search for the node.
        while current_node is not None:
            # Check if current node has a matching key.
            if current_node.key == key:
                if current_node.left is None and current_node.right is None:
                    if parent is None:
                        self.root = None
                    elif parent.left is current_node:
                        parent.left = None
                    else:
                        parent.right = None
                    return
                elif current_node.left is not None and current_node.right is None:
                    if parent is None:
                        self.root = current_node.left
                    elif parent.left is current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return
                elif current_node.left is None and current_node.right is not None:
                    if parent is None:
                        self.root = current_node.right
                    elif parent.left is current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    return
                else:
                    # Find successor (leftmost child of right subtree)
                    successor = current_node.right
                    while successor.left is not None:
                        successor = successor.left
                    current_node.key = successor.key
                    parent = current_node
                    current_node = current_node.right
                    key = parent.key
            # Search right.
            elif current_node.key < key:
                parent = current_node
                current_node = current_node.right
            # Search left.
            else:
                parent = current_node
                current_node = current_node.left
        return

class AVLTree:
    class AVLNode:
        # Constructor with a key paramater creates the Node object.
        def __init__(self, key):
            self.key = key
            self.parent: AVLTree.AVLNode | None = None
            self.left: AVLTree.AVLNode | None = None
            self.right: AVLTree.AVLNode | None = None
            self.height = 0

        # Calculate the current nodes' balance factor, defined as height (left subtree) - height (right subtree).
        def get_balance(self):
            # Get current height of left subtree, or -1 if None.
            left_height = -1
            if self.left is not None:
                left_height = self.left.height
            # Get current height of right subtree, or -1 if None.
            right_height = -1
            if self.right is not None:
                right_height = self.right.height
            # Calculate the balance factor.
            return left_height - right_height

        # Recalculate the current height of the subtree rooted at the node, usually called after a subtree has been modified.
        def update_height(self):
            # Get current height of left subtree, or -1 if None.
            left_height = -1
            if self.left is not None:
                left_height = self.left.height
            # Get current height of right subtree, or -1 if None.
            right_height = -1
            if self.right is not None:
                right_height = self.right.height
            # Assign self.height with calculated node.
            self.height = max(left_height, right_height) + 1

        # Assign either the left or right data member with a new child.
        # The parameter which_child is expected to be the string "left" or the string "right".
        # Returns True if the new child is successfully assigned to this node, False otherwise.
        def set_child(self, which_child, child):
            # Ensure which_child is properly assigned.
            if which_child != 'left' and which_child != 'right':
                return False
            # Assign the left or right data member.
            if which_child == 'left':
                self.left = child
            else:
                self.right = child
            # Assign the parent data member of the new child, if the child is not None.
            if child is not None:
                child.parent = self
            # Update the node's height, since the subtree's structure may have changed.
            self.update_height()
            return True

        # Replace a current child with a new child.
        # Determines if the current child is on the left or right, and calls set_child() with the new node appropriately.
        # Returns True if the new child is assigned, False otherwise.
        def replace_child(self, current_child, new_child):
            if self.left is current_child:
                return self.set_child('left', new_child)
            elif self.right is current_child:
                return self.set_child('right', new_child)
            # If neighter of the above casess applied, then the new child could not be attached to this node.
            return False

    # Constructor to create an empty AVLTree.
    # There is only one data member, the tree's root Node, and it starts out as None.
    def __init__(self):
        self.root: AVLTree.AVLNode | None = None

    # Performs a left rotation at the given node.
    # Returns the new root of the subtree.
    def rotate_left(self, node: AVLNode):
        # Define a convience pointer to the left child of the right child.
        right_left_child: AVLTree.AVLNode = node.right.left
        # Step 1 - the right child moves up to the node's position.
        # This detaches node from the tree, but it will be reattached later.
        if node.parent is not None:
            node.parent.replace_child(node, node.right)
        # Node is root.
        else:
            self.root = node.right
            self.root.parent = None
        # Step 2 - the node becomes the left child of what used to be its right child, but is now its parent.
        # This will detach right_left_child from the tree.
        node.right.set_child('left', node)
        # Step 3 - reattach right_left_child as the right child of node.
        node.set_child('right', right_left_child)
        return node.parent

    # Performs a right rotation at the given node.
    # Returns the subtree's new root.
    def rotate_right(self, node: AVLNode):
        # Define a convenience pointer to the right child of the left child.
        left_right_child = node.left.right
        # Step 1 - the left child moves up to the node's position.
        # This detaches node from the tree, but it will be reattached later.
        if node.parent is not None:
            node.parent.replace_child(node, node.left)
        # Node is root.
        else:
            self.root = node.left
            self.root.parent = None
        # Step 2 - the node becomes the right child of what used to be its left child, but is now its parent.
        # This will detach left_right_child from the tree.
        node.left.set_child('right', node)
        # Step 3 - reattach left_right_child as the right child of the node.
        node.set_child('left', left_right_child)
        return node.parent

    # Updates the given node's height and rebalances the subtree if the balancing factor is now -2 or +2.
    # Rebalancing is done by performing a rotation.
    # Returns the subtree's new root if a rotation occurred, or the node if no rebalancing was required.
    def rebalance(self, node: AVLNode):
        # First update the height of this node.
        node.update_height()
        # Check for an imbalance.
        if node.get_balance() == -2:
            # The subtree is too big to the right.
            if node.right.get_balance() == 1:
                # Double rotation case.
                # First do a right rotation on the right child.
                self.rotate_right(node.right)
            # A left rotation will now make the subtree balanced.
            return self.rotate_left(node)
        elif node.get_balance() == 2:
            # The subtree is too big to the left.
            if node.left.get_balance() == -1:
                # Double rotation case.
                # First do a left rotation on the left child.
                self.rotate_left(node.left)
            # A right rotation will now make the subtree balanced.
            return self.rotate_right(node)
        # No imbalance, so just return the original node.
        return node

    def insert(self, node: AVLNode):
        # Special case: if the tree is emppty, just set the root to the new node.
        if self.root is None:
            self.root = node
            node.parent = None
        else:
            # Step 1 - do a regular binary search tree insert.
            current_node = self.root
            while current_node is not None:
                # Choose to go left or right
                if node.key < current_node.key:
                    # Go left.
                    # If left child is None, insert the new node here.
                    if current_node.left is None:
                        current_node.left = node
                        node.parent = current_node
                        current_node = None
                    else:
                        # Go left and do the loop again.
                        current_node = current_node.left
                else:
                    # Go right.
                    # If the right child is None, insert the new node here.
                    if current_node.right is None:
                        current_node.right = node
                        node.parent = current_node
                        current_node = None
                    else:
                        # Go right and do the loop again.
                        current_node = current_node.right

            # Step 2 - rebalance along a path from the new node's parent up to the root.
            node = node.parent
            while node is not None:
                self.rebalance(node)
                node = node.parent

    def remove_node(self, node: AVLNode | None):
        # Base case:
        if node is None:
            return False
        # Parent needed for rebalancing.
        parent = node.parent
        # Case 1: internal node with 2 children.
        if node.left is not None and node.right is not None:
            # Find successor.
            successor_node = node.right
            while successor_node.left != None:
                successor_node = successor_node.left
            # Copy the value from the node.
            node.key = successor_node.key
            # Recursively remove successor
            self.remove_node(successor_node)
            # Nothing left to do since the recursive call will have rebalanced.
            return True
        # Case 2: root node (with 1 or 0 children).
        elif node is self.root:
            if node.left is not None:
                self.root = node.left
            else:
                self.root = node.right
            if self.root is not None:
                self.root.parent = None
            return True
        # Case 3: internal with left child only.
        elif node.left is not None:
            parent.replace_child(node, node.left)
        # Case 4: internal with right child only OR leaf.
        else:
            parent.replace_child(node, node.right)
        # Node is gone.
        # Anything that was below node that has persisted is already correctly balanced, but ancestors of node may need rebalancing.
        node = parent
        while node is not None:
            self.rebalance(node)
            node = node.parent
        return True

    # Searches for a node with a matching key.
    # Does a regular binary search tree search operation.
    # Returns the node with the matching key if it exists in the tree, or None if there is no matching key in the tree.
    def search(self, key):
        current_node = self.root
        while current_node is not None:
            # Compare the current node's key with the target key.
            # If it is a match, return the current key.
            # Otherwise, go either to the left or right, depending whether the current node's key is smaller or larger than the target key.
            if current_node.key == key: return current_node
            elif current_node.key < key: current_node = current_node.right
            else: current_node = current_node.left

    # Attempts to remove a node with a matching key.
    # If no node has a matching key then nothing is done and False is returned.
    # Otherwise the node is removed and True is returned.
    def remove_key(self, key):
        node = self.search(key)
        if node is None:
            return False
        else:
            return self.remove_node(node)
