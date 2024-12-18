# Algorithm Notes:

## Algorithm Definition:
A process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer.

## Algorithm Guidelines:
- The steps in the algorithm need to be in a very specific order.
- The steps in the algorithm need to be distinct.
- The steps in the algorithm should produce a result.
- The algorithm should complete in a finite amount of time.

## NP-Complete Problems:
NP-complete problems are a set of problems for which no known efficient algorithm exists and have the following characteristics:

- No efficient algorithm has been found to solve an NP-complete problem.
- No one has proven that an efficient algorithm to solve an NP-complete problem is impossible.
- If an efficient algorithm exists for one NP-complete problem, then all NP complete problems can be solved efficiently.

By knowing a problem is NP-complete, instead of trying to find an efficient algorithm to solve the problem, a programmer can focus on finding an algorithm to efficiently find a good, but non-optimal solution.

## Complexity:
Algorithm complexity is the combination of a multitude of factors, mainly space and time complexity, both of which can be written using big O notation.
When written this way the algorithm can be simplified for comparison against other algorithms.

### Time Complexity:
Time complexity is a measure of the amount of computational time that an algorithm takes to complete as a function of the size of the input data.
It is used to evaluate the efficiency of an algorithm and to predict its performance.

#### Key Points:
- Big O Notation: Time complexity is often expressed using Big O notation, which provides an upper bound on the running time of an algorithm.
- Factors: Time complexity considers the number of elementary operations performed by the algorithm as a function of the input size.
- Worst, Average, and Best Case: Time complexity can describe the worse-case, average-case, and best-case scenarios for the algorithm's running time.

### Space Complexity:
Space Complexity is a measure of the amount of memory space that an algorithm requires to run to completion as a funciton of the size of the input data.
It evaluates the efficiency of an algorithm in terms of memory usage.

#### Key Points:
- Memory Usage: Space complexity considers both the auxiliary space (extra space or temporary space used by an algorithm) and the input space (the space required to store the input data).
- Big O Notation: Space complexity is often expressed using Big O notation.
- Factors: Space complexity takes into account variables, data structures, call stack size for recursive algorithms, and any dynamic memory allocations made during the execution of the algorithm.

### Big O Notation:
Big O notation is a mathmatical notation used to describe the performance or complexity of an algorithm.
Specifically, it characterizes the behavior of an algorithm as the input size grows, providing a high-level understanding of its efficiency in terms of time or space requirements.

Big O notation provides a way to describe the efficiency of algorithms in a standardized manner, allowing comparisons based on their growth rates.
Understanding Big O notation helps in evaluating and choosing appropriate algorithms based on the expected input size and performance requirements.

#### Key Concepts:
1. Worst-case Scenario: Big O notation typically describes the worst-case scenario, representing the upper bound on the time or space on algorithm will require.
2. Input size (N): The variable N usually denotes the size of the input to the algorithm, such as the number of elements in a list.
3. Growth Rate: Big O notation expresses how the runtime or space requirements grow as the input size increases. It focuses on the most significant terms and ignores constant factors and lower-order terms.

#### Common Classifications:
1. O(1) - Constant: The runtime or space does not change with the size of the input.
2. O(log N) - Logarithmic: The runtime or space grows logarithmically with input size. This often occurs in algorithms that are recursive.
3. O(N) - Linear: The runtime or space grows linearly with the input size. This often occurs in algorithms that are iterative.
4. O(N log N) - Linearithmetic (Log-Linear): The runtime or space grows in proportion to N times the logarithm of N. Many efficient sorting algorithms have this complexity.
5. O(N<sup>2</sup>) - Quadratic: The runtime or space grows quadratically with the input size. This is common with algorithms containing nested loops.
6. O(C<sup>N</sup>) - Exponential: The runtime or space grows exponentially with the input size. Algorithms with this complexity are usually impractical for large inputs.
7. O(N!) - Factorial: The runtime or space grows factorially with input size. This is often seen in algorithms that generate all permutations of a set.

#### Ignoring Constants and Lower-Order Terms:
Big O notation simplifies the analysis by focusing on the dominant term and ignoring the constants and lower-order terms.
For example, an algorithm with a complexity of 5N<sup>2</sup> + 3N + 10 is considered O(N<sup>2</sup>) because, as N grows, the N<sup>2</sup> term will dominate the growth rate.

## Recurrance Relations:
A recurrance relation is a function that is defined in terms of the same function operating on a value < N, such as the function T(N) = O(1) + T(N / 2).
Using O-notation to express runtime complexity of a recursive function requires solving the recurrance relation.

### Recursion Tree:
A recursion tree is a useful tool for solving recurrances. It is a visuall diagram of an operation done by a recursive function that separates operations done directly by the function and operations done by recursive calls.

## Fast Sorting Algorithms:
A fast sorting algorithm is a sorting algorithm that has an average runtime complexity of O(N log N) or better.

### Sorting Algorithms' Average Runtime Complexity:
|Sorting Algorithm|Average case runtime complexity|Fast?|
|-----------------|-------------------------------|-----|
|Selection sort   |O(N<sup>2</sup>)               |No   |
|Insertion sort   |O(N<sup>2</sup>)               |No   |
|Shell sort       |O(N<sup>1.5</sup>)             |No   |
|Quicksort        |O(N log N)                     |Yes  |
|Merge sort       |O(N log N)                     |Yes  |
|Heap sort        |O(N log N)                     |Yes  |
|Radix sort       |O(N)                           |Yes  |

### Element Comparison Sorting Algorithm:
A element comparison sorting algorithm is a sorting algorithm that operates on an array of elements that can be compared to each other.

#### Identifying Comparison Sorting Algorithms:
|Sorting algorithm|Comparison?|
|-----------------|-----------|
|Selection sort   |Yes        |
|Insertion sort   |Yes        |
|Shell sort       |Yes        |
|Quicksort        |Yes        |
|Merge sort       |Yes        |
|Heap sort        |Yes        |
|Radix sort       |No         |

### Fast Sorting Algorithm's Best, Average, and Worst Case Runtime Complexity:
|Sorting algorithm|Best cases runtime complexity|Average case runtime complexity|Worst case runtime complexity|
|-----------------|-----------------------------|-------------------------------|-----------------------------|
|Quicksort        |O(N log N)                   |O(N log N)                     |O(N<sup>2</sup>)             |
|Merge sort       |O(N log N)                   |O(N log N)                     |O(N log N)                   |
|Heap sort        |O(N)                         |O(N log N)                     |O(N log N)                   |
|Radix sort       |O(N)                         |O(N)                           |O(N)                         |

## Selection Sort Algorithm:
Selection sort is a sorting algorithm that treats the input as two parts, sorted and unsorted, and repeatedly selects the proper next value to move from the unsorted part to the end of the sorted part.

1. The index variable i denotes the dividing point. Elements to the left of i are sorted, and elements including and to the right of i are unsorted.
2. All elements in the unsorted part are searched to find the index of the next element with the smallest value.
3. The variable index_smallest stores the index of the smallest element in the unsorted part.
4. Once the element with the smallest value is found, the element is swapped with the element at locattion i.
5. Then, the index i is advanced one place to the right, and the process repeats.

The term "selection" comes from the fact that for each iteration of the outer loop, a value is selected for position i.

Typical runtime complexity of O(N<sup>2</sup>).

## Insertion Sort Algorithm:
Insertion sort is a sorting algorithm that treats the input as two parts, sorted and unsorted, and repeatedly inserts the next value from the unsorted part into the correct location in the sorted part.

1. The index variable i denotes the starting position of the current element in the unsorted part.
2. Initially, the first element is assumed to be sorted, so the outer loop initializes to 1.
3. The inner while loop inserts the current element into the sorted part by repeatedly swapping the current element with the elements in the sorted part.
4. Once a smaller or equal element is found in the sorted part, the current element has been inserted in the correct location and the while loop terminates.

Typical runtime complexity of O(N<sup>2</sup>).

For sorted or nearly sorted inputs the runtime complexity is O(N).

## Shell Sort:
Shell sort is a sorting algorithm that treats the input as a collection of interleaved lists, and sorts each list individually with a variant of the insertion sort algorithm, using gap values to determine the number of interleaved lists.

A gap value is a positive integer representing the distance between elements in an interleaved list.
For each interleaved list, if an element is at index i, the next element is at index i + gap value

- Begins by choosing a gap value K and sorting K interleaved lists in place.
- Finishes by performing a standard insertion sort on the entire array.
- Since the interleaved parts have been sorted, smaller elements will be close to the array's beginning and larger elements towards the end.
- Insertion sort can then quickly sort the nearly sorted array.

In the case the array size is not evenly divisible by the gap value, some interleaved lists will have fewer items than others.

- Begins by picking an arbitrary collection of gap values. For each gap value K, K calls are made to the insertion sort variant function to sort K interleaved lists.
- Ends with a final gap value of 1, to finish with the regular insertion sort
- Tends to perform well when choosing gap values in descending order.
- A common option is to choose powers of 2 minus 1, in descending order.
- Using gap values that are powers of 2 or in descending order is not required. Shell sort will correctly sort arrays using any positive integer gapp values in any order, provided a gapp value of 1 is included.

Typical runtime complexity of O(N<sup>3/2</sup>) or O(N<sup>1.5</sup>).

## Quicksort
Quicksort is a sorting algorithm that repeatedly partitions the input into low and high parts (each unsorted), and then recursively sorts each of those parts.To partition the input, quicksort chooses a pivot to divide the data into low and high parts.
All values in the low partition are less than or equal to the pivot value.
All values in the high partition are greater than or equal to the pivot value.
Values equal to the pivot may appear on either or both of the partitions.
The pivot can be any value within the array, commonly the value of the middle array element.

- The partitioning algorithm uses two index variables, l and h (low and high), initialized to the left and right sides of the current sorted elements.
- As long as the value at index l is lesss than the pivot value, the algorithm increments l, because the element should remain in the low partition.
- As long as the value at index h is greater than the pivot value, the algorithm decrements h, becaause the element should remain in the high partition.
- Then, if l >= h, all elements have been partitioned, and the partitioning algorithm returns h, which is the index of the last element in the low partition.
- Otherwise, the elements at indicies l and h are swapped to move those elements to the correct partions.
- The algorithm then increments l, decrements h, and repeats.
- Typically implemented as a recursive algorithm using calls to quicksort the low and high partitions.
- This recursive sorting process continuess until a partition has one or zero elements, and thus is already sorted.

Typical runtime complexity of O(N log N) if equal partioning occurs, otherwise runtime complexity will be O(N<sup>2</sup>), which rarely occurs.

## Quickselect:
Quickselect is an algorithm that selects the k<sup>th</sup> smallest element in a list.

For a list with N elements, quickselect uses quicksort's partition function to partition the list into a low partition containing the X smallest elementss and a high partition containing N - X largest elements.
The k<sup>th</sup> smallest element in the low partition f k is less than or qual to the last index in the low partioin, and in the high partion otherwise.
Quickselect is recursively called on the partition that contains the  k<sup>th</sup> element.
When a partition size 1 is encountered, quickselect has found the k<sup>th</sup> smallest element.

Quickselect partially sorts the list when selecting the k<sup>th</sup> smallest element.

The best and average case runtime complexity of quickselect are both O(N).
In worst case, quickselect may sort the entire list, resulting in a runtime of O(N<sup>2</sup>)

## Merge Sort:
Merge sort is a sorting algorithm that divides a list into two halves, recursively sorts each half, and then merges the sorted halves to produce a sorted list. The recursive partitioning continues until a list of one element is reached, as a list of one element is already sorted.

The merge sort algorithm uses three index variables to keep track of the elements to  sort for each recursive call:
- The index variable i is the index of the first element in the list.
- The index variable k is the index of the last element.
- The index variable j is used to divide the list into two halves.
- Elements from i to j are in the left half, and elements from j + 1 to k are in the right half.

Merge sort merges the two sorted partitions into a single list by repeatedly selecting the smallest element from either the left or right partition and adding that element to a temporary merged list.
Once fully merged, the elements in the temporary merged list are copied back to the original list.

Typical runtime complexity of O(N log N).
Typical space complexity of O(N).

## Bubble Sort:
Bubble sort is a sorting algorithm that iterates through a list, comparing and swapping adjacent elements if the second element is less than the first.

Uses nested loops resulting in a runtime complexity of O(N<sup>2</sup>).

Often considered impractical for real-world use since many faster sorting algorithms exist.

## Bucket Sort:
Bucket sort is a numerical sorting algorithm that distributes numbers into buckets, sorts each bucket with an additional sorting algorithm, and then concatenates buckets together to build the sorted result.

A bucket is a container for numerical values in a specific range.

1. The algorithm creates a list of buckets, each representing a range of numerical values.
Collectively, the buckets represent the range from 0 to the max value in the array.
For N buckets and a max value of M, each bucket represents x values: $$ x = \frac{M + 1}{N} $$
The bucket index is calculated as: $$ [number * \frac{N}{M + 1}] $$
2. Then, each bucket is sorted with an additional sorting algorithm.
3. Lastly, all buckets are concatenated together in order and copied to the original array.

## Radix Sort:
Radix sort is a sorting algorithm designed specifically for integers.
The algorithm makes use of a concept called buckets and is a type of bucket sort.

A bucket is a collection of integer values that all share a particular digit value.

Radix sort is a sorting algorithm specifically for an array of integers:
- The algorithm processes one digit at a time starting with the least significant digit and ending with the most significant.
- Two steps are needed for each digit:
    1. First, all array elements are placed into buckets based on the current digit's value.
    2. Then, the array is rebuilt by removing all elements from buckets, in order from lowest bucket to highest.


## Huffman compression:
Given data represented as some quantity of bits, compression transforms the data to use fewer bits.
Compressed data uses less storage and can be communicated faster than uncompressed data.

The basic idea of compression is to encode frequently-occuring items using fewer bits.

Prior to compression, a character frequency table must be built for an input string.
Such a table contains each distinct character from the input string and each character's number of occurances.
Programming languages commonly provide a dictionary or map object to store the character frequency table.

Huffman coding is a common compression technique that assigns fewer bits to frequent items, using a binary tree.

Note: For Huffman encoded data, the dictionary must be included along with the compressed data, to enable decompression.

### Building a Huffman Tree:
The data members in a Huffman tree node depend on the node type:
- Leaf nodes have two data members: a character from the input and an integer frequency for that character.
- Internal nodes have left and right child nodes, along with an integer frequency value that represents the sum of the left and right child frequencies.

A Huffman tree can be built from a charactter frequency table.
Each character corresponds to a leaf node.
The Huffman code for a character is built by tracing a path from the root to that character'ss leaf node, appending 0 when branching left or 1 when right.

### Compressing Data:
To compress an input string, the Huffman codes are first obtained for each character.
Then each character of the input string is processed and corresponding bit codes are concatenated to produce the compressed result.

### Decompressing Huffman Coded Data:
To decompress Huffman code data, one can use a Huffman tree and trace the branches for each bit, starting at the root.
When the final node of the branch is reached, the result has been found.
The processs continues until the entire item is decompressed.

## Heuristics:
In practice, solving a problem in the optimal or most accurate way may require more computational resources than are available or feasible.
Algorithms implemented for such problems often use a heuristic.
A heuristic is a technique that willingly accepts a non-optimal or less accurate solution in order to improve execution speed.

A heuristic algorithm is an algorithm that quickly determines a near optimal or approximate solution.

A self-adjusting heuristic is an algorithm that modifies a data structure based on how that data structure is used.

### Greedy Algorithm:
A greedy algorithm solves a problem by assuming that the optimal choice at a given moment during the algorithm will also be the optimal choice overall.
Greedy algorithms tend to be efficient, but certain types of problems exist where greedy algorithms don't find the best or optimal solution.
However, greedy algorithms produce both effcient and optimal solutions for many problems.

## Dynamic Programming:
Dynamic programming is a problem solving technique that:
1. Splits a problem into smaller subproblems.
2. Computes and stores solutions to subproblems in memory.
3. Uses the stored solutions to solve the larger problem.
