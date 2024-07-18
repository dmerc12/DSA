# Heaps and Treaps:
## Heaps:
Some applications require fast access to and removal of the maximum item in a changing set of items.

### Max-Heap:
A max-heap is a complete binary tree that maintains the simple property that a node's key is greater than or equal to the node's children's keys
(Actually, a max-heap may be any tree, but is commonly a binary tree).
Because x &ge; y and y &ge; z implies x &ge; z, the property results in a node's key being greater than or equal to all the node's descendant's keys.
Therefore, a max-heap's root always has the maximum key in the entire tree.

#### Max-Heap Insert and Remove Operations:
An insert into a max-heap starts by inserting the node in the tree's last level, and then swapping the node with its parent until no max-heap property violation occurs.
Inserts fill a level (left-to-right) before adding another level, so the tree's height is always the minimum possible.
The upward movement of a node in a max-heap is called percolating.

A remove from a max-heap is always a removal of the root, and is done by replacing the root with the last level's last node, and swapping that node with its greatest child until no max-heap property violation occurs.
Because upon completion that node will occupy another node's location (which was swapped upwards), the tree height remains the minimum possible.

### Mini-Heap:
A mini-heap is similar to a max-heap, but a node's key is less than or equal to its children's keys.

### Heaps using Arrays:
Heaps are typically stored using arrays.
Given a tree representation of a heap, the heap's array form is produced by traversing the tree's levels from left to right and top to bottom.
The root node is always the entry at index 0 in the array, the root's left child is the entry at index 1, and so on.

Because heaps are not implemented with node structures and parent / child pointers, traversing from a node to parent or child nodes requires referring to nodes by index.
The table below shows parent and child index formulas for a heap.
#### Parent and Child Indices for a Heap:
|Node index|Parent index |Child indicies      |
|----------|-------------|--------------------|
|0         |N/A          |1, 2                |
|1         |0            |3, 4                |
|2         |0            |5, 6                |
|3         |1            |7, 8                |
|4         |1            |9, 10               |
|5         |2            |11, 12              |
|...       |...          |...                 |
|i         |[(i - 1) / 2]|2 * i + 1, 2 * i + 2|

### Heap Sort:
Heapsort is a sorting algorithm that takes advantage of a max-heap's propertiess by repeatedly removing the max and building a sorted array in reverse order.
An array of unsorted values must first be converted into a heap.
The heapify operation is used to turn an array into a heap.
Since leaf nodes already satisfy the max heap property, heapifying to build a max-heap is achieved by percolating down on every non-leaf node in reverse order.

The heapify operation starts on the internal node with the largest index and continuess down to, and including, the root node at index 0.
Given a binary tree with N nodes, the largest internal node index is [N / 2] - 1.

Heapsort begins by heapifying the array into a max-heap and initializing an end index value to the size of the array minus 1.
Heapsort repeatedly removes the maximum value, stores that value at the end index, and decrements the end index.
The removal loop repeats until the end index is 0.

Heapsort uses 2 loops to sort an array.
The first loop heapifies the array using MaxHeapPercolateDown.
The second loop removes the maximum value, stores that value at the end index, and decrements the end index, until the end index is 0.

#### Max-Heap Largest Internal Node Index:
|Number of nodes in binary heap|Largest internal node index|
|------------------------------|---------------------------|
|1                             |-1 (no internal nodes)     |
|2                             |0                          |
|3                             |0                          |
|4                             |1                          |
|5                             |1                          |
|6                             |2                          |
|7                             |2                          |
|...                           |...                        |
|N                             |[N / 2] - 1                |
