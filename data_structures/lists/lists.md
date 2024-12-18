# Lists

## List ADT:
A list is a common ADT for holding ordered data, and having operations such as:
- Append a data item.
- Remove a data item.
- Search whether a data item exists.
- Print the list.

A common approach for implementing a linked list is using two data structures:
1. List data structure: A list data structure is a data structure containing the list's head and tail, and may also include additional information.
2. List node data structure: The list node data structure maintains the data for each list element, including the element's data and pointers to the other list element.

A list data structure is not required to implement a linked list, but offers a convient way to store the list's head and tail.
When using a list data structure, functions that operate on a list can use a single parameter for the list's data structure to manage the list.

A linked list can also be implemented without using a list data structure, which minimally requires using separate list node pointer variables to track.

### Common Operations for a List ADT:
|Operation              |Description                              |Example starting with list: 99, 77                               |
|-----------------------|-----------------------------------------|----------------------------------                               |
|Append(list, x)        |Inserts x at end of the list.            |Append(list, 44), list: 99, 77, 44                               |
|Prepend(list, x)       |Inserts x at start of the list.          |Prepend(list, 44), list: 44, 99, 77                              |
|InsertAfter(list, w, x)|Inserts x after w.                       |InsertAfter(list, 99, 44), list: 99, 44, 77                      |
|Remove(list, x)        |Removes x.                               |Remove(list, 77), list: 99                                       |
|Search(list, x)        |Returns item if found, else returns null.|Search(list, 99), returns item 99, Search(list, 22), returns null|
|Print(list)            |Prints list's items in order.            |Print(list) outputs: 99, 77                                      |
|PrintReverse(list)     |Prints list's items in reverse order.    |PrintReverse(list) outputs: 77, 99                               |
|Sort(list)             |Sorts the lists items in ascending order.|Sort(list) alters list to: 77, 99                                |
|IsEmpty(list)          |Returns true if lisst has no items.      |IsEmpty(list) returns false                                      |
|GetLength(list)        |Returns the number of items in the list. |GetLength(list) returns 2                                        |

## Singly-Linked Lists:
A singly-linked list is a data structure for implementing a list ADT, where each node has data and a pointer to the next node.
The list structure typically has pointers to the list's first and last node.
A singly-linked list's first node is called the head, and the last node the tail.
A singly Linked list is a type of positional list, where elements contain pointers to the next and / or previous elements in the list.

### Appending a Node to a Singly-Linked List:
Given a new node, the append operation for a singly-linked list inserts the new node after the list's tail node.
The append algorithm behavior differs if the list is empty versus not empty:
- Append to empty list: If the list's head pointer is null (empty), the algorithm points the list's head and tail pointers to the new node.
- Append to non-empty list: If the list's head pointer is not null (not empty), the algorithm points the tail node's next pointer and the list's tail pointer to the new node.

### Prepending a Node to a Singly-Linked List:
Given a new node, the prepend operation for a singly-linked list inserts the new node before the list's head node.
The prepend algorithm behavior differs if the list is empty versus not empty:
- Append to empty list: If the list's head pointer is null (empty), the algorithm points the list's head and tail pointers to the new node.
- Append to non-empty list: If the list's head pointer is not null (not empty), the algorithm points the new node's next pointer to the head node, and then points the list's head pointer to the new node.

### Inserting a Node into a Singly-Linked List:
Given a new node, the InsertAfter operation for a singly-linked list inserts the new node after a provided existing list node.
curNode is a pointer to an existing list node, but can be null when inserting into an empty list.
The InsertAfter algorithm considers three insertion scenarios:
- Insert as list's first node: If the list's head pointer is null, the algorithm points the list'ss head and tail pointers to the new node.
- Insert after list's tail node: If the list's head pointer is not null (list not empty) and curNode points to the list's tail node, the algorithm points the tail node's next pointer and the list's tail pointer to the new node.
- Insert in middle of list: If the list's head pointer is not null (list not empty) and curNode does not point to the list's tail node, the algorithm points the new node's next pointer to curNode's next node, and then points curNode's next pointer to the new node.

### Removing a Node in a Singly-Linked List:
Given a specified existing node in a singly-linked list, the RemoveAfter operation removes the node after the specified list node.
The existing node is specified with the curNode parameter.
If curNode is null, RemoveAfter removes the list's first node.
Otherwise, the algorithm removes the node after curNode.

- Remove list's head node (special case): Iff curNode is null, the algorithm points sucNode to the head node's next node, and points the list's head pointer to sucNode. If sucNode is null, the only list node was removed, so the list's tail pointer is pointed to null (indicating the list is now empty).
- Remove node after curNode: If curNode's next pointer is nottt null (a node after curNode exists), the algorithm points sucNode to the node after curNode's next node. Then curNode's next pointer is pointed to sucNode. If sucNode is null, the list's tail node was removed, so the algorithm points the list's tail pointer to curNode (the new tail node).

### Searching for a Node in a Singly-Linked List:
Given a key, a search algorithm returns the first node whose data matches that key, or returns null if a matching node was not found.
A simple linked list search algorithm checks the current node (initially the list's head node), returning that node if a match, else pointing the current node to the next node and repeating.
If the pointer to the current node is null, the algorithm returns null (matching node was not found).

## Doubly-Linked Lists:
A doubly-linked list is a data structure for implementing a list ADT, where each node has data and a pointer to both the next node and the previous node.
The list structure typically points to the first node as well as the last node.
The doubly-linked list's first node is called the head, and the last node the tail.

A doubly-linked list is similar to a singly-linked list, but instead of using a single pointer to the next node in the list, each node has a pointer to the next and previous nodes.
A doubly-linked list is also a type of positional list, where elements contain pointers to the next and / or previous elements in the list.

### Appending a Node to a Doubly-Linked List:
Given a new node, the Append operation for a doubly-linked list inserts the new node after the list's tail node.
The algorithm behavior differs if the list is empty versus not empty:
- Append to empty list: If the list's head pointer is null (empty), the algorithm points the list's head and tail pointers to the new node.
- Append to a non-empty list: If the list's head ppointer is not null (not empty), the algorithm points the tail node's next pointer to the new node, points the new node's previous pointer to the list's tail node, and points the list's tail pointer to the new node.

### Prepending a Node to a Doubly-Linked List:
Given a new node, the Prepend operation of a doubly-linked list inserts the new node before the list's head node and points the head pointer to the new node.
- Prepend to empty list: If the list's head pointer is null (empty), the algorithm points the list's head and tail pointers to the new node.
- Prepend to non-empty list: If the list's head pointer is not null (not empty), the algorithm points the new node's next pointer to the list's head node, points the list's head node's previous pointer to the new node, and then points the list's head pointer to the new node.

### Inserting into a Doubly-Linked List:
Given a new node, the InsertAfter operation for a doubly-linked list inserts the new node after a provided existing list node.
curNode is a pointer to an existing list node.
The InsertAfter algorithm considers three insertion scenarios:
- Insert as first node: If the list's head pointer is null (list is empty), the algorithm points the list's head and tail pointers to the new node.
- Insert after list's tail node: If the list's head pointer is not null (list not empty) and curNode points to the list's tail node, the new node is inserted after the tail node. The algorithm points the tail node's next pointer to the new node, points the new node's previous pointer to the list's tail node, and then points the list's tail pointer to the new node.
- Insert in middle of list: If the list's head pointer is not null (list is not empty) and curNode does not point to the list's tail node, the algorithm updates the current, new, and successor nodes' next and previous pointers to achieve the ordering {curNode newNode sucNode}, which requires four pointer updates: point the new node's next pointer to sucNode, point the new node's previous pointer to curNode, point curNode's next pointer to the new node, and point sucNode's previous pointer to the new node.

### Removing a Node in a Doubly-Linked List:
The Remove operation for a doubly-linked list removes a provided existing list node.
curNode is a pointer to an existing list node.
The algorithm first determines the node's successor (next node) and predecessor (previous node).
The variable sucNode points to the successor, predNode points to the predecessor.
The algorithm uses four separate checks to update each pointer:
- Successor exists: If the successor node pointer is not null (successor exists), the algorithm points the successor's previous pointer to the predecesssor node.
- Predecessor exists: If the predecessor node pointer is not null (predecessor exists), the algorithm points the predecessor's next pointer to the successor node.
- Removing the list's head node: If curNode points to the list's head node, the algorithm points the list's head pointer to the successor node.
- Removing the list's tail node: If curNode points to the list's tail node, the algorithm points the list's tail pointer to the predecessor node.

When removing a node in the middle of the list, both the predecessor and successor nodes exist, and the algorithm updates the predecesssor and successor nodes' pointers to achieve the ordering {predNode sucNode}.
When removing the only node in a list, curNode points to both the list's head and tail nodes, and sucNode and predNode are both null.

## Circular Lists:
A circular linked list is a linked list where the tail node's next pointer points to the head of the list instead of null.
A circular linked list can be used to represent repeating processes.

The head of a circular linked list is often referred to as the start node.

A traversal through a circular linked list is similar to traversal through a standard linked list, but must terminate after reaching the head node a second time, as opposed to terminating when reaching null.

## Linked List Traversal:
A list traversal algorithm visits all nodes in the list once and performs an operation on each node.
The algorithm starts by pointing a curNode pointer to the list's head node.
While curNode is not null, the algorithm performs an operation then points curNode to the next node.
After the list's tail node is visited, curNode is pointed to the tail node's next node, which is null, so traversal ends.
The traversal algorithm supports both singly-linked and doubly-linked lists.

A doubly-linked list also supports reverse traversal.
Reverse traversal visits all nodes starting with the list's tail node and ending after visiting the list's head node.

## Sorting Linked Lists:
### Insertion Sort for Doubly-Linked Lists:
Insertion sort for a doubly-linked list operates similarly to thye insertion sort algorithm used for arrays.
Starting with the second list element, each element in the linked list is visited.
Each visited element is moved back as needed and inserted into the correct position in the list's sorted portion.
The list must be a doubly-linked list, since reverse traversal is not possible with a singly-linked list.

### Insertion Sort for Singly-Linked Lists:
Insertion sort can sort a singly-linked list by changing how each visited element is inserted into the sorted portion of tthe list.
The insertion sort algorithm can find the insertion position by traversing the list from the list head toward the current element.
The FindInsertionPosition algorithm searches the list for the insertion position and returns the list node after which the current node should be inserted.
If the current node should be inserted at the head, FindInsertionPosition returns null.

### Sorting Linked-Lists vs. Arrays:
Sorting algorithms for arrays (quicksort and heapsort) require constant-time access to arbitrary, indexed locations to operate efficiently.
Linked lists do not allow indexed access, making for difficult adaptation of such sorting algorithms to operate on linked lists.
The talbes below provide a brief overview of the challenges in adappting array sorting algorithms for linked lists.

#### Sorting Algorithms Easily Adapted to Efficiently Sort Linked Lists:
|Sorting algorithm|Adaption to linked lists|
|-----------------|------------------------|
|Insertion sort   |Operates similarly on doubly-linked lists. Requires searching from the head of the list for an element's insertion possition for singly-linked lists.|
|Merge sort       |Finding the middle of the list requires searching linearly from the head of the list. The merge algorithm can also merge lists without additional storage.|

#### Sorting Algorithms Difficult to Adapt to Efficently Sort Linked Lists:
|Sorting algorithm|Challenge|
|-----------------|---------|
|Shell sort       |Jumping the gap between elements cannot be done on a linked list, as each element between two elements must be traversed.|
|Quicksort        |Partitioning requires reverse traversal through the right portion of the array, which is not supported with singly-linked lists.|
|Heap sort        |Indexed access is required to find child nodes in constant time when percolating down.|

## Linked List Dummy Nodes:
A linked list implementation may use a dummy node (or header node).
A header node is a node with an unused data member that always resides at the head of the list and cannot be removed.
Using a dummy node simplifiess the algorithms for a linked list becausse the head and tail pointers are never null.
An empty list consists of the dummy node, which has the next pointer set to null and the list's head and tail pointers both point to the dummy node.

### Singly-Linked List Implementation:
When a singly-linked list with a dummy node is created, the dummy node is allocated and the list's head and tail pointers are set to point to the dummy node.
List operations are simpler to implement compared to a linked list without a dummy node, since a special case is removed from each implementation.

### Doubly-Linked List Implementation:
A dummy node can also be used in a doubly-linked list implementation.
The dummy node in a doubly-linked list always has the prev pointer set to null.

A doubly-linked list implementation can also use two dummy nodes: one at the head and the other at the tail.
Doing so removes additional conditionals and further simplifies the implementation of most methods.

## Recursion in Linked Lists:
### Forward Traversal:
Forward traversal through a linked list can be implemented using a recursive function that takes a node as an argument.
If non-null, the node is visited first.
Then, a recursive call is made on the node's next pointer, to traverse the remainder of the list.
The ListTraverse function takes a list as an argument, and searches the entire list by calling ListTraverseRecursive on the list's head.

### Searching:
A recursive linked list search is implemented similar to forward traversal.
Each call examines one node.
If the node is null, then null is returned.
Otherwise, the node's data is compared to the search key.
If a match occurs, the node is returned, otherwise the remainder of the list iss searched recursively.

### Reverse Traversal:
Forward traversal visits a node first, then recursively traverses the remainder of the list.
If the order is swapped, such that the recursive call is made first, the list is traversed in reverse order.

## Array-Based Lists:
An array-based list is a list ADT implemented using an array.
An array-based list supports the common list ADT operations.

In many programming languages, arrays have a fixed size.
An array-based list implementation will dynamically allocate the array as needed as the number of elements changes.
Initially, the array-based list implementation allocates a fixed size array and uses a length variable to keep track of how many array elements are in use.
The list starts with a default allocation size, greater than or equal to one. A default size of one to ten is common.

Given a new element, the append opperation for an array-based list of length X inserts the new element at the end of the list, or at index X.

### Resize Operation:
An array-based list must be resized if an item is added when the allocation size equals the list length.
A new array is allocated with a length greater than the existing array.
Allocating the new array with twice the current length is a common approach.
The existing array elements are then copied to the new array, which becomes the list's storage array.

Because all existing elements must be copied from one array to another, the resize operation has a runtime complexity of O(N).

### Prepend and Insert After Operations:
The Prepend operation for an array-based list inserts a new item at the start of the list.
- First, if the allocation size equals the list length, the array is resized.
- Then, all existing array elements are moved up by one position, and the new item is inserted at the list start or index zero.
- Because all existing array elements must be moved up by one, the Prepend operation has a runtime complexity of O(N).

The InsertAfter operation for an array-based list inserts a new item after a specified index.
- First, if the allocation size equals the list length, the array is resized.
- Next, all elements in the array residing after the specified index are moved up by one position.
- Then, the new item is inserted at index (specified index + 1) in the list's array.
- The InsertAfter operation has a best case runtime complexity of O(1) and a worst case runtime complexity of O(N).

### Search and Removal Opertions:
Given a key, the search operation returns the index for the first element whose data matches that key, or -1 if not found.

Given the index of an item in an array-based list, the remove-at operation removed the item at that index.
When removing an item at index X, each item after index X is moved down by one position.

Both the search and remove operations have a worst case runtime complexity of O(N).
