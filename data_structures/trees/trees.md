# Trees:
Trees are commonly used to represent hierarchical data.
A tree can represent file and directories in a file system, since a file system is a hierarchy.

## Binary Trees:
In a binary tree, each node has up to 2 children, known as a left child and a right child.
"Binary" means two, referring to the two children.
Some more definitions related to a binary tree:
- Leaf: A tree node with no children.
- Internal Node: A node with at least one child.
- Parent: A node with a child is said to be that child's parent.
A node's ancestors include the node's parent, the parent's parent, etc., up to the tree's root.
- Root: The one tree node with no pparent (the "top" node).
- Edge: The link from a node to a child.
- A node's depth is the number of edges on the path from the root to the node.
The root node thus has a depth of 0.
- All nodes with the same depth form a tree level.
- A tree's height is the largest depth of any node.
A tree with just one node has a height of 0.

Certain binary tree structures can affect the speed of operations on the tree.
The following describe special types of binary trees:
- A binary tree is full if every node contains 0 or 2 children.
- A binary tree is complete if all levels, except possibly the last level, contain all possible nodes and all nodes in the last level are as far left as possible.
A binary tree is perfect, if all internal nodes have 2 children and all leaf nodes are on the same level.

## Binary Space Partitioning (BSP):
BSP is a technique of repeatedly separating a region of space into two parts and cataloging objects contianed within the regions.
A BSP tree is a binary tree used to store information for binary space partitioning.
Each node in a BSP tree contains information about a region of space and chich objects are contained in the region.

In graphics applications, a BSP tree can be used to store all objects ina multidimensional world.
The BSP tree can then be used to efficiently determine which objects must be rendered on screen.
The viewer's position in space is used to perform a lookup within the BSP tree.
The loopup quickly eliminates a large number of objects that are not visible and therefore should not be rendered.

## Binary Search Trees (BST):
An especially useful form of binary tree is a BST, which has an ordering property that any node's left subtree keys &le; the node's key, and the right subtree's keys &ge; the node's key.
That property enables fast searching for an item to be shown later.

To search nodes means to find a node with a desired key, if such a node exists.
A BST may yield faster searches than a list.
Searching a BST starts by visiting the root node.
If a child to be visited doesn't exist, the desired node doesn't exist.
With this approach, only a small fraction of nodes need be compared.

Searching a BST in the worst case requires H + 1 comparisons, meaning O(H) comparisons, where H is the tree height.
A major BST benefit is that an N-node binary tree's height may be as small as O(log N), yielding extremely fast searches.
A binary tree's height can be minimized by keeping all levels full, except possibly the last level.
Such an "all-but-last-level-full" binary tree's height is H = [log<sub>2</sub> N].

A BST defines an ordering among nodes, from smallest to largest.
A BST node's successor is the node that comes after in the BST ordering.
A BST node's predecessor is the node that comes before in the BST ordering.

### BST Search Algorithm:
Given a key, a search algorithm returns the first node found matching that key, or returns null if a matching node is not found.
A simple BST search algorithm checks the current node (initially the tree's root), returning that node as a match, else assigning the current node with the left (if key is less) or right (if key is greater) child and repeating.
If such a child is null, the algorithm returns null (matching note not found).

### BST Insert Algorithm:
Given a new node, a BST insert operation inserts the new node in a proper location obeying the BST ordering property.
A simple BST insert algorithm compares the new node with the current node (initially the root).
- Insert as left child: If the new node's key is less than the current node, and the current node's left child is null, the algorithm assigns that node's left child with the new node.
- Insert as right child: If the new node's key is greater than or equal to the current node, and the current node's right child is null, the algorithm assigns the node's right child with the new node.
- Search for insert location: If the left (or right) child is not null, the algorithm assigns the current node with that child node and continues searching for a proper insert location.

### BST Remove Algorithm:
Given a key, a BST remove operation removes the first-found matching node, restructuring the tree to preserve the BST ordering property.
The algorithm first searches for a matching node just like the search algorithm.
If found (call this node X), the algorithm performs one of the following sup-algorithms:
- Remove a leaf node: If X has a parent (so X is not the root), the parent's left or right child (whichever points to X) is assigned with null.
Else, if X was the root, the root pointer is assigned with null, and the BST is now empty.
- Remove an internal node with single child: If X has a parent (so X is not the root), the parent's left or right child (whichever points to X) is assigned with X's single child.
Else, if X was the root, the root pointer is assigned with X's single child.
- Remove an internal node with 2 children: This case is the hardest.
First the algorithm locates X's successsor (the leftmost child of X's right subtree), and copies the successor to X.
Then, the algorithm recursively removes the successor from the right subtree.

### BST In Order Traversal:
A tree traversal algorithm visits all nodes in the tree once and performs an operation on each node.
An inorder traversal visits all nodes in a BST from smallest to largest.
Starting from the root, the algorithm recursively traverses the left subtree, the current node, and the right tree.

### BST Height and Insertion Order:
Recall that a tree's height is the maximum edges from the root to any leaf (a one-node tree has a height of 0).
The minimum N-node binary tree height is <i>h = [log<sub>2</sub> N]</i>, achieved when each level is full except possibly the last.
The maximum N-node binary tree height is <i>N - 1</i> (the - 1 is because the root is at height 0).

Searching a BST is fast if the tree's height is near the minimum.
Inserting items in random order naturally keeps a BST's height near the minimum.
In contrast, inserting items in nearly-sorted order leads to a nearly-maximum tree height.

Given a node representing a BST subtree, the height can be computed as follows:
- If the node is null, return -1.
- Otherwise recursively compute the left and right child subtree heights, and return 1 plus the greater of the 2 child subtrees' heights.

### BST Parent Node Pointers:
A BST implementation often includes a parent pointer inside each node.
A balanced BST, such as an AVL tree or red-black tree, may utilize the parent pointer to traverse up the tree from a particular node to find a node's parent, grandparent, or siblings.

### BST Recursion:
### BSST Recursive Search Algorithm:
BST search can be implemented using recursion.
A single node and search key are passed as arguments to the recursive search function.
Two base cases exist.
1. When the node is null, in which cases null is returned.
If the node is non-null, then the search key is compared to the node's key.
2. When the search key equals the node's key, in which case the node is returned.
If the search key is less than the node's key, a recursive call is made on the node's left child.
If the search key is greater than the node's key, a recursive call is made on the node's right child.

### BST Get Parent Algorithm:
A recursive BST get-parent algorithm searches for a parent in a way similar to the normal BST search algorithm.
Instead of comparing the search key with a candidate node's key, the search key is compared with the keys of the candidate node's children.

### Recursive BST Insertion and Removal:
BST insertion and removal can also be implemented using recursion.
The insertion algorithm uses recursion to traverse down the tree until the insertion location is found.
The removal algorithm uses the recursive search functions to find the node and the node's parent, then removes the node from the tree.
If the node to remove is an internal node with two children, the node's successor is recursively removed.

## Tries:
A trie (prefix tree) is a tree representing a set of strings.
Each non-root node represents a single character.
Each node has at most one child per distinct alphabet character.
A terminal node is a node representing a terminating character, which is the end of a string in the trie.

Tries provide efficient storage and quick search for strings, and are often used to implement auto-complete and predictive text input.

### Trie Insert Algorithm:
Given a string, a trie insert operation creates a path from the root to a terminal node that visits all the string's characters in sequence.
A current node pointer initially points to the root.
A loop then iterates through the string's characters.
For each character:
1. A new child node is added only if the current node does not have a child for the character.
2. The current node pointer is assigned with the current node's child for the character.

After all characters are pprocessed, a terminal node is added and returned.

### Trie Search Algorithm:
Given a string, a trie search operation returns the terminal node corresponding to that string, or null if the string is not in the trie.

### Trie Remove Algorithm:
Given a string, a trie remove operation removes the string's corresponding terminal node and all non-root ancestors with 0 children.

## AVL Tree:
An AVL tree is a BST with a height balance property and specific operations to rebalance the tree when a node is inserted or removed.
A BST is height balanced if for any node, the heights of the node's left and right subtrees differ by only 0 or 1.
A node's balance factor is the left subtree height minus the right subtree height, which is 1, 0, or -1 in an AVL tree.
For calculating a balance factor, a non-existent left or right child's subtree's height is said to be -1.

### AVL tree height:
Minimizing binary tree height yields fastest searches, insertions, and removals.
If nodes are inserted and removed dynamically, maintaining a minimum height tree requires extensive tree rearrangements.
In contrast, an AVL tree only requires a few local rotations, so is more computationally efficient, but doesn't guarantee a minimum height.
However, theoreticians have shown that an AVL tree's worst case height is no worse than 1.5X the minimum binary tree height, so the height is still O(log N) where N is the number of nodes.
Furthermore, experiments show that AVL tree heights in practice are much closer to the minimum.

### Storing Height at Each AVL Node:
An AVL tree implementation can store the subtree height as a member of each node.
With the height stored as a member of each node, the balance factor for any node can be computed in O(1) time.
When a node is inserted in or removed from an AVL tree, ancestor nodes may need the height value to be recomputed.

### AVL Rotations:
Inserting an item into an AVL tree may require rearranging the tree to maintain height balance.
A rotation is a local rearrangement of a BST that maintains the BST ordering property while rebalancing the tree.
Rotating is said to be done "at" a node.
A rotation can be done left or right.

### Algorithms Supporting AVL Trees:
The AVLTreeUpdateHeight algorithm updates a node's height value by taking the maximum of the child subtree heights and adding 1.
The AVLTreeSetChild algorithm sets a node as the parent's left or right child, updates the child's parent pointer, and updates the parent node's height.
The AVLTreeReplaceChild algorithm replaces one of a node's existing child pointers with a new value, utilizing AVLTreeSetChild to perform the replacement.
The AVLTreeGetBalance algorithm computes a node's balance factor by subtracting the right subtree height from the left subtree height.

### Rotation Algorithms:
This works for right or left rotations.

A right rotation algorithm is definied on a subtree root (node D) which must have a left child (node B).
The algorithm reassigns child pointers, assigning B's right child with D, and assigning D's left child with C (B's original right child, which may be null).
If D's parent is non-null, then the parent's child D is replaced with B.
Other parts naturally stay with their parent nodes.

A left rotation algorithm is defined on a subtree root (node D) which must have a right child (node B).
The algorithm reassigns child pointers, assigning B's right child with D, and assigning D's left child with C(B's original left child, which may be null).
If D's parent is non-null, then the parent's child is replaced with B.
Other parts naturally stay with their parent nodes.

### AVL Tree Balancing:
When an AVL tree node has a balance factor of 2 or -2, which only occurs after an insertion or removal, the node must be rebalanced via rotations.
The AVLTreeRebalance algorithm updates height value at a node, computes the balance factor, and rotates if the balance factor is 2 or -2.

### AVL Insertions:
Inserting an item into an AVL tree may cause the tree to become unbalanced.
A rotation can rebalance the tree.

Sometimes, the imbalance is due to an insertion on the inside of the subtree, rather than on the oustside.
One rotation won't rebalance.
A double rotation is needed.

After inserting a node, nodes on the path from the new node to the root should be checked for a balance factor of 2 or -2.
The first susch node P triggers rebalancing.
Four cases exist, distinguishable by the balance factor of node P and one of P's children.

An AVL tree insertion involves searching for the insert location, inserting the new node, updating balance factors, and rebalancing.

Balance factor updates are only needed on nodes ascending along the path from the inserted node up to the root, since no other nodes' balance could be affected.
Each node's balance factor can be recomputed by determining left and right subtree heights, or for speed can be stored in each node and then incrementally uppdated : +1 if ascending from a left child, -1 if from a right child.
If a balance factor update yields 2 or -2, the imbalance case is determined via that node's left (for 2) or right (for -2) child's balance factor, and the appropriate rotations performed.

