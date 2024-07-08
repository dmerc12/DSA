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
