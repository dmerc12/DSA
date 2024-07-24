# B-Trees:
In a binary tree, each node has one key and up to two children.
A B-tree with order K is a tree where nodes can have up to K-1 keys and up to K children.
The order is the maximum number of children a node can have.
B-trees have the following properties:
- All keysin a B-tree must be distinct.
- All leaf nodes must be at the same level.
- An internal node with N keys must have N + 1 children.
- Keys in a node are stored in sorte order from smallest to largest.
- Each key in a B-tree internal node has one left subtree and one right subtree.
All left subtree keys are < that key, and all right subtree keys are > that key.

As the order of a B-tree increases, the maximum number of keys and children per node increases.
An internal node must have one more child than keys.
Each  child of an internal node can have a different number of keys than the parent internal node

## 2-3-4 Trees:
A 2-3-4 tree is an order 4 B-tree.
Therefore, a 2-3-4 tree node contains 1, 2, or 3 keys.
A leaf node in a 2-3-4 tree has no children.

The keys and children in a 2-3-4 tree node are commonly referred to by index.
So keys are called key 0, key 1, and key 2, and children are called child 0, child 1, child 2, and child 3.
If a node has one key, then keys 1 and 2 and children 2 and 3 are not used.
If a node contains 2 keys, then key 2 and child 3 are not used.
A 2-3-4 tree node containing three keys is said to be full.

A node with one key is called a 2-node.
A node with two keys is called a 3-node.
A node with three keys is called a 4-node.

### Search Algorithm:
Given a key, a search algorithm returns the first node found matching that key, or returns null if a matching node is not found.
Searching a 2-3-4 tree is a recursive process that starts with the root node.
If the search key equals any of the keys in the node, then the node is returned.
Otherwise, a recursive call is made on the appropriate child node.
Which child node is used depends on the value of the search key in comparison to the node's keys.
The table below shows conditions, which are checked in order, and the corresponding child nodes.

### Tree Child Node to Choose Based on Search Key:
|Condition|Child node to search|
|---------|--------------------|
|key < node's A key|left|
|node has only 1 key or key < node's B key|middle1|
|node has only 2 keys or key < node's C key|middle 2|
|none of the above|right|

### Insert Algorithm:
Given a new key, a 2-3-4 tree insert operation inserts the new key in the proper location ssuch that all 2-3-4 tree properties are preserved.
New keys are always inserted into leaf nodes in a 2-3-4 tree.
Insertion returns the leaf node where the key was inserted, or null if the key was already in the tree.

An important operation during insertion is the split operation, which is done on every full node encountered during insertion traversal.
The split operation moves the middle key from a child node into thte child's parent node.
The first and last keys in the child node are moved into two separate nodes.
The split operation returns the parent node that recieved the middle key from the child.

Splitting an internal node allocates 2 new nodes, each with a single key, and the middle key from the split node moves up into the parent node.
Splitting the root node allocates 3 new nodes, each with a single key, and the root of the tree becomes a new node with a single key.

During a split operation, any non-full internal node may need to gain a key from a split child node.
This skey may have children on either side.

A new key is always inserted into a non-full leaf node.
The table below describes the 4 possible cases for inserting a new key into a non-full leaf node.

### Tree Non-Full-Leaf Insertion Cases:
|Condition|Outcome|
|---------|-------|
|New key equals an existing key in node|No insertion takes place, and the node is not altered|
|New key is < node's first key|Existing keys in node are shifted right, and the new key becomes node's first key|
|Node has only 1 key or new key is < node's middle key|Node's middle key, if present, becomes last key, and new key becomes node's middle key|
|None of the above|New key becomes node's last key|

Multiple insertion schemes exist for 2-3-4 trees.
The preemptive split insertion scheme always splits any full node encountered during insertion traversal.
The preemptive split insertion scheme ensures that any time a full node is split, the pparent node has room to accomodate the middle value from the child.

### Removal:
Removing an item from a 2-3-4 tree may require rearranging keys to maintain tree properties.
A rotation is a rearrangement of keys between 3 nodes that maintains all 2-3-4 tree properties in the process.
The 2-3-4 tree removal algorithm uses rotations to transfer keys between sibling nodes.
A right rotation on a node causes the node to lose one key and the node's right sibling to gain one key.
A left rotation on a node causes the node to lose one key and the node's left sibling to gain one key.

Several utility functions are used in the rotation operation:
- BTreeGetLeftSibling returns a pointer to the left sibling of a node or null if the node has no left sibling.
BTreeGetLeftSibling returns null, left, middle1, or middle2 if the node is the left, middle1, middle2, or the right child of the parent, respectively.
Since the parent node is required, a precondition of this function is that the node is not the root.
- BTreeGetRightSibling returns a pointer to the right sibling of a node or null if the node has no right sibling.
- BTreeGetParentKeyLeftOfChild takes a parent node and a child of the parent node as arguments, and returns the key in the parent that is immediately left of the child.
- BTreeSetParentKeyLeftOfChild takes a parent node, a child of the parent node, and a key as arguments, and sets the key in the parent that is immediately left of the child.
- BTreeAddKeyAndChild operates on a non-full node, adding one new key and one new child to the node.
The new key must be greater than all keys in the node, and all keys in the new child subtree must be greater than the new key.
- BTreeRemoveKey removes a key from a node using a key index in the range [0, 2].
This process may require moving keys and children to fill the location left by removing the key.

The rotation algorithm operates on a node, causing a net decrease of 1 key in that node.
The key removed from the node moves up into the parent node, displacing a key in the parent that is moved to a sibling.
No new nodes are allocated, nor existing nodes deallocated during the rotation.
The code simply copies key and child pointers.

### Fusion:
When rearranging values in a 2-3-4 tree during deletions, rotations are not an option for nodes that do not have a sibling with 2 or more keys.
Fusion provides an additional option for increasing the number of keys in a node.
A fusion is a combination of 3 keys: 2 from adjacent sibling nodes that have 1 key each, and a third from the parent of the siblings.
Fusion is the inverse operation of a split.
The key taken from the parent node must be the key that is between the 2 adjacent siblings.
The parent node must have at least 2 keys, with the exception of the root.

Fusion of the root node is a special case that happens only when the root and the root's 2 children each have 1 key.
In this case, the 3 keys from the 3 nodes are combined into a single node that becomes the new root node.

### Non-Root Fusion:
For the non-root case, fusion operates on 2 adjacent siblings that each have 1 key.
The key in the parent node that is between the 2 adjacent siblings is combined with the 2 keys from the two siblings to make a single, fused node.
The parent node must have at least 2 keys.

### Merge Algorithm:
A B-Tree merge operates on a node with 1 key and increases the node's keys to 2 or 3 ussing either a rotation or fusion.
A node's 2 adjacent siblings are checked first during a merge, and if either has 2 or more keys, a key is transferred via a rotation.
Such a rotation increases the number of keys in the merged node from 1 to 2.
If all adjacent siblings of the node being merged have 1 key, then fusion is used to increases the number of keys in the node from 1 to 3.
The merge operation can be performed on any node that has 1 key and a non-null parent node with at least 2 keys.

Several utility functions are used in a B-tree remove operation:
- BTreeGetMinKey returns the minimum key in a subtree.
- BTreeGetChild returns a pointer to a node's left, middle1, middle2, or right child, if the childIndex argument is 0, 1, 2, or 3, respectively.
- BTreeNextNode returns the child of a node that would be visited next in the traversal to search for the specified key.
- BTreeKeySwap swaps one key with another in a subtree.
The replacement key must be known to be a key that can be used as a replacement without violating any of the 2-3-4 tree rules.

### Remove Algorithm:
Given a key, a 2-3-4 tree remove operation removes the first-found matching key, restructuring the tree to preserve all 2-3-4 tree rules.
Each successful removal results in a key being removed from a leaf node.
Two cases are possible when removing a key, the first being that the key resides in a leaf node, and the second being that the key resides in an internal node.

A key can only be removed from a leaf node that has 2 or more keys.
The preemptive merge removal scheme involves increasing the number of keys in all single-key, non-root nodes encountered during traversal.
The merging always happens before any key removal is attempted.
Preemptive merging ensues that any leaf node encountered during removal will have 2 or more keys, allowing a key to be removed from the leaf node without violating the 2-3-4 tree rules.

To remove a key from an internal node, the key to be removed is replaced with the minimum key in the right child subtree (known as the key's successor), or the maximum key in the leftmost child subtree.
First, the key chosen for replacement is stored in a temporary variable, then the chosen key is removed recursively, and lastly the temporary key replaces the key to be removed.
