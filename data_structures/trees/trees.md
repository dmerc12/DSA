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

Insertion starts with the standart BST insertion algorithm.
After inserting a node, all ancestors of the inserted node, from the parent up to the root are rebalanced.
A node is rebalanced by first computing the node's balance factor, then performing rotations if the balance factor is outside of the range [-1, 1].

### AVL Removals:
Given a key, an AVL tree remove operation removes the first-found matching node, restructuring the tree to preserve all AVL tree requirements.
Removal begins by removing the node ussing the standard BST removal algorithm.
After removing a node, all ancestors of the removed node, from the nodes' parent up to the root, are rebalanced.
A node is rebalanced by first computing the node's balance factor, then performing rotations if the balance factor is 2 or -2.

To remove a key, the AVL tree removal algorithm first locates the node containing the key using BSTSearch.
If the node is found, AVLTreeRemoveNode is called to remove the node.
Standard BST removal logic is used to remove the node from the tree.
Then AVLTreeRebalance is called for all ancestors of the removed node, from the parent up to the root.

## Red-Black Tree - A Balanced Tree:
A red-black tree is a BST with two node types, namely red and black, and supporting opperations that ensure the tree is balanced when a node is inserted or removed.
The below red-black tree's requirements ensure that a tree with N nodes will have a height of O(log N).
- Every node is colored either red or black.
- The root node is black.
- A red node's children cannot be red.
- A null child is considered to be a black leaf node.
- All paths from a node to any null leaf descendant node must have the same number of black nodes.

### Rotations:
A rotation is a local rearangment of a BST that maintains the BST ordering property while rebalancing the tree.
Rotations are used during the insert and remove operations on a red-black tree to ensure that the red-black tree requirements hold.
Rotating is said to be done "at" a node.
A left rotation at a node causes the node's right child to take the node's place in the tree.
A right rotation at a node causes the node's left child to take the node's place in the tree.

A rotation requires altering up to three child subtree pointers.

A left rotation at a node requires the node's right child to be non-null.
Two utility funcitons are used for red-black tree rotations.
The RBTreeSetChild utility function sets a node's left child, if the whichChild parameter is "left", or right child, if the whichChild parameter is "right", and updates the child's parentt pointer.
The RBTreeReplaceChild utility funciton replaces a node's left or right child pointer with a new value

The RBTreeRotateLeft function performs a left rotation at the specified node by updating the right child's left child to point to the node, and updating the node's right child to point to the right child's former left child.
If non-null the node's parent has the child pointer changed from node to the node's right child.
Otherwise, if the node's parent is null, then the tree's root pointer is updated to point to the node's right child.

Right rotation is analgous to left rotation.
A right rotation at a node requires the node's left child to be non-null.

### Insertion:
Given a new node, a red-black tree insert operation inserts the new node in the proper location such that all red-black tree requirements still hold after the insertion completes.
Red-black tree insertion begins by calling BSTInsert to insert the node using the BST insertion rules.
The newly inserted node is colored red and then a balance operation is performed on this node.
The red-black balance operation consists of the steps below:
1. Assign parent with node's parent, uncle with node's uncle, which is a sibling of parent, and grandparent with node's grandparent.
2. If node is the tree's root, then color node black and return.
3. If parent is black, then return without any alterations.
4. If parent and uncle are both red, then color parent and uncle black, color grandparent red, recursively balance grandparent, then return.
5. If node is parent's right child and parent is grandparent's left child, then rotate left at parent, assign node with parent, assign parent with node's parent, and continue at step 7.
6. If node is parent's left child and parent is grandparent's right child, then rotate right at parent, assign node with parent, assign parent with node's parent, and continue at step 7.
7. Color parent black and grandparent red.
8. If node is parent's left child, then rotate right at grandparent, otherwise rotate left at grandparent.

### Removal:
Given a key, a red-black tree remove operation removes the first-found matching node, restructuring the tree to preserve all red-black tree requirements.
First the node to remove is found using BSTSearch.
If the node is found, RBTreeRemoveNode is called to remove the node.

Given a key, a red-black tree remove-key operation removes the key from the tree, if present, restructuring as needed to preserve all red-black tree requirements.
First, BSTSearch is called to find the node containing the key.
If the node is found, RBTreeRemoveNode() is called to remove the node.
RBTreeRemoveNode() consists of the following steps:
1. If the node has two children, copy the key from the node's predecessor to a temporary value, recursively remove the predecessor from the tree, replace the node's key with the temporary value, and return.
2. If the node is black, call RBTreePrepareForRemoval() to restructure the tree in preparation for the node's removal.
3. Remove the node using the standard BST removal algorithm.

Utility funcitons help simplify red-black tree removal code.
The RBTreeGetSibling function returns the sibling of a node.
The RBTreeIsNonNullAndRed function returns true only if a node is non-null and red, false otherwise.
The RBTreeIsNullOrBlack function returns true if a node is null or black, false otherwise.
The RBTreeAreBothChildrenBlack function returns true only if both of a node's children are black.
Each utility function considers a null node to be a black node.

Preparation for removing a black node requires altering the number of black nodes along paths to preserve the black-path-length property.
The RBTreePreppareForRemoval algorithm uses six utility functions that analyze the tree and make appropriate alterations when each of the six cases is encountered.
The utility functions return true if the case is encountered, and false otherwise.
If case one, three, or four is encountered, RBTreePrepareForRemoval will return after calling the utility function.
If case two, five, or six is encountered, additional cases must be checked.

Preparation for removing a node first checks for each of the six cases, performing the operations below:
1. If the node is red or the node's parent is null, then return.
2. If the node has a red sibling, then color the parent red, and the sibling black.
If the node is the parent's left child then rotate left at the parent, otherwise rotate right at the parent.
Continue to the next step.
3. If the node's parent is black and both children of the node's sibling are black, then color the sibling red, recursively call on the node's parent, then return.
4. If the node's parent is red and both children of the node's sibling are black, then color the parent black, color the sibling red, then return.
5. If the sibling's left child is red, the sibling's right child is black, and the node is the left child of the parent, then color the sibling red and the left child of the sibling black.
Then rotate right at the sibling and continue to the next step.
6. If the sibling's left child is black, the sibling's right child is red, and the node is the righ child of the parent, then color the sibling red and the right child of the sibling black.
Then rotate left at the sibling and continue to the next step.
7. Color the sibling the same color as the parent and color the parent black.
8. If the node is the parent's left child, then color the sibling's right child black and rotate left at the parent.
Otherwise color the sibling's left child black and rotate right at the parent.

#### Prepare-For-Removal Algorithm Case Descriptions:
|Case #|Condition|Action if condition true|Process additional cases after action?|
|------|---------|------------------------|--------------------------------------|
|1|Node is red or node's parent is null|None|No|
|2|Sibling node is red|Color parent red and sibling black. If node is left child of parent, rotate left at parent node, otherwise rotate right at parent node|Yes|
|3|Parent is black and both of sibling's children are black|Color sibling red and call removal preparation function on parent|No|
|4|Parent is red and both of sibling's children are black|Color parent black and sibling red|No|
|5|Sibling's left child is red, sibling's right child is black, and node is left child of parent|Color sibling red and sibling's left child black. Rotate right at sibling|Yes|
|6|Sibling's left child is black, sibling's right child is red, and node is right child of parent|Color sibling red and sibling's right child black. Rotate left at sibling|Yes|
