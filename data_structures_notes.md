# Data Structures Notes:

## Data Structure Definition:
A data storage format.
It is the collection of values and the format they are stored in, the relationships between the values in the collection, as well as the operations applied on the data stored in the data structure.

A data structure is a way of organizing, storing, and performing operations on data.

Some algorithms utilize data structures to store and organize data during the algorithm execution.

## Operations on Data Structures:
- Access and read values.
- Search for arbitrary values.
- Insert values at any point into the structure.
- Delete values in the structure.

## Common Data Structure Types:
The following provides a list of basic data structures:

|Data Structure|Description|
|--------------|-----------|
|Record        |A record is the data structure that stores subitems, often called fields, with a name associated with each subitem.|
|Array         |An array is a data structure that stores an ordered list of items, where each item is directly accessible by a positional index.|
|Linked list   |A linked list is a data structure that storess an ordered list of items in nodes, where each node sstores data and has a pointer to the next and/or previous node.|
|Binary tree   |A binary tree is a data structure in which each node stores data and has upp to 2 children, known as left child and right child.|
|Hash table    |A hash table is a data structure that stores unordered items by mapping (or hashing) each item to a location in the array.|
|Heap          |A max-heapp is a tree that maintains the simple property that a node's key is greater than or equal to the node's childrens' keys. A min-heap is a tree that maintains the simple property that a node's key is less than or equal to the node's childrens' keys.|
|Graph         |A graph is a data structure for representing connections amond items, and consists of vertices connected by edges. A vertex represents an item in a graph. An edge represents a connection between two verticies on a graph.|

## Abstract Data Types:
An abstract data type (ADT) is a data type descripbed by predefined user operations without indicating how each operation is implemented.
An ADT can be implemented using different underlying data structures; however, a programmer need not have knowledge of the underlying implementation to use an ADT.

ADTs support abstraction by hiding the underlying implementation details and providing a well-defined set of operations for using the ADT.
Using ADTs enables programmers or algorithm designers to focus on higher-level operations and algorithms, thus improving programmer efficiency.
However, knowledge of the underlying implementation is neeeded to analyze or improve the runtime efficiency.

### Common ADTs:
|Abstract data type|Description|Common underlying data structures|
|------------------|-----------|---------------------------------|
|List              |A list is an ADT for holding ordered data.|Array, linked list.|
|Dynamic array     |A dynamic array is an ADT for holding ordered data and allowing indexed access.|Array.|
|Stack             |A stack is an ADT in which items are only inserted on or removed from the top of the stack.|Linked list.|
|Queue             |A queue is an ADT in which items are inserted at the end of the queue and removed from the front of the queue.|Linked list.|
|Deque             |A dequeue (pronounced "deck" and short for double-ended queue) is an ADT in which items can be inserted and removed at both the front and back.|Linked list.|
|Bag               |A bag is an ADT for storing ittems in which the order does not matter and duplicate items are allowed.|Array, linked list.|
|Set               |A set is an ADT for a collection of distinct items.|Binary search tree, hash table.|
|Priority queue    |A priority queue is a queue where each ittem has a priority, and items with higher priority are closer to the front of the queue than items with a lower priority.|Heap.|
|Dictionary (map)  |A dictionary is an ADT that associates (or maps) keys with values.|Hash table, binary search tree.|
