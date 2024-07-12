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

### BST Height and Insertion Order:

### BST Parent Node Pointers:

### BST Recursion:

## Tries:
