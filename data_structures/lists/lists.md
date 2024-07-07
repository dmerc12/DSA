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

