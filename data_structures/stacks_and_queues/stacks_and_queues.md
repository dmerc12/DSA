# Stacks and Queues:

## Stack ADT:
A stack iss an ADT in which items are only inserted on or removed from the top of the stack.
The stack push operation inserts an item on the top of the stack.
The stack pop operation removes and returns the item at the top of the stack.
A stack is referred to as a last-in-first-out(LIFO) ADT.

A stack can be implemented using a linked list, an array, or a vector.

### Common Stack ADT Operations:
|Operation       |Description                                     |Example starting with stack: 99, 77 (top is 99)|
|----------------|------------------------------------------------|-----------------------------------------------|
|Push(stack, x)  |Inserts x on top of stack                       |Push(stack, 44). Stack: 44, 99, 77             |
|Pop(stack)      |Returns and removes item at top of stack        |Pop(stack) returns 99. Stack: 77               |
|Peep(stack)     |Returns but does not remove item at top of stack|Peep(stack) returns 99. Stack still: 99, 77    |
|IsEmpty(stack)  |Returns true if stack has no items              |IsEmpty(stack) returns false                   |
|GetLength(stack)|Returns the number of items in the stack        |GetLength(stack) returns 2                     |

### Linked List Stack:
A stack is often implemented using a linked list, with the list's head node being the stack's top.
A push is performed by creating a new list node, assigning the node's data with the item, and prepending the node to the list.
A pop is performed by assigning a local variable with the head node's data, removing the head node from the list, and then returning the local variable.

### Array-Based Stacks:
A stack can be implemented with an array.
Two variables are needed in addition to the array:
- allocationSize: an integer for the array's allocated size.
- length: an integer for the stack's length.

The stack's bottem item is at array[0] and the top at array[length - 1].

#### Unbounded Stack:
An unbounded stack is a stack with no upper limit on length.
An unbounded stack's length can increase indefinitely, so the stack's array allocation size must also be able to increase indefinitely.

#### Bounded Stack:
A bounded stack is a stack with a length that does not exceed a maximum value.
The maximum is comonly the initial allocation size.
A bounded stack with a length equal to the maximum length is said to be full.

## Queue ADT:
A queue is an ADT in which items are inserted at the end of the queue and removed from the front of the queue.
The queue enquque operation inserts an item at the end of the queue.
The queue dequque opperation removes and returns the item at the front of the queue
A queue is referred to as a first-in-first-out (FIFO) ADT.

A quque can be implemented using a linked list or an array.

### Common Queue ADT Operations:
|Operation        |Description                                           |Example starting with queue: 43, 12, 77 (front is 43)|
|-----------------|------------------------------------------------------|-----------------------------------------------------|
|Enqueue(queue, x)|Inserts x at end of the queue                         |Enque(queue, 56). Queue: 43, 12, 77, 56              |
|Dequque(queue)   |Returns and removes item at front of queue            |Dequeue(queue) returns: 43. Queue: 12, 77            |
|Peek(queue)      |Returns but does not remove item at the front of queue|Peek(queue) returns 43. Queue: 43, 12, 77            |
|IsEmpty(queue)   |Returns true is queue has no items                    |IsEmpty(queue) returns false                         |
|GetLength(queue) |Returns the number of items in the queue              |GetLength(queue) returns 3                           |

### Linked List Queue:
A queue is often implemented using a linked list, with the list's head node representing the queue's front, and the list's tail node representing the queue's end.
Enqueueing an item is performed by creating a new list node, assigning the node's data with the item, and appending the node to the list.
Dequeueing is performed by assigning a local variable with the head node's data, removing the head node from the list, and returning the local variable.

### Array-Based Queue:
A queue can be implemented with an array.
Two variables are needed in addition to the array:
- length: an integer for the queue's length.
- front_index: an integer for the queue's front item index.

A queue's content starts at array[front_index] and continues forward through length items.
If the array's end is reached before encountering all items, remaining items are stored starting at index 0.

### Bounded vs Unbounded Queue:
A bounded queue is a queue with a length that does not exceed a specified maximum value.
An additional variable, max_length, is needed.
max_length is commonly assigned at construction time and does not change for the queue's lifetime.
A bounded queue with a length equal to the maximum length is said to be full.

An unbounded queue is a queue with a length that can grow indefinitely.
