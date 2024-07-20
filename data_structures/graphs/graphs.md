# Graphs:
A graph is a data structure for representing connections among items, and consists of vertices connected by edges.
- A vertex (or node) represents an item in a graph.
- An edge represents a connection between two verticies in a graph.

For a given graph, the number of vertices is commonly represented as V, and the number of edges as E.
In a graph:
- Two vertices are adjacent if connected by an edge.
- A path is a sequence of edges leading from a source (starting) vertex to a destination (ending) vertex.
The path length is the number of edges in the path.
- The distance between two vertices is the number of edges on the shortest path between those vertices.

## Application of Graphs:
### Geographic Maps and Navigation:
Graphs are often used to represent a geographic map, which can contain information about places and travel routes.
Edge weights in such graphs often represent the length of a travel route, either in total distance or expected time taken to navigate the route.

### Product Recommendations:
A graph can be used to represent relationships between products.
Vertices in the graph corresponding to a customer's purchased products have adjacent vertices represesnting products that can be recommended to the user.

### Social and Professional Networks:
A graph may use a vertex to represent a person.
An edge in such a graph represents a relationship between two people.
In a graph representing a social network, an edge commonly represents friendship.
In a graph representing a professional network, an edge commonly represents business conducted between two people.

## Adjacency Lists:
Various approaches exist for representing a graph data structure.
A common approach is an adjacency list.
Recall that two vertices are adjacent if connected by an edge.
In an adjacency list graph representation, each vertex has a list of adjacent vertices, each list item representing an edge.

### Advantages of Adjacency Lists:
A key advantage of an adjacency list graph representation is a size of O(V + E), because each vertex appears once, and each edge appears twice.
V refers to the number of vertices, E the number of edges.

However, a disadvantage is that determining whether two vertices are adjacent is O(V), because one vertex's adjacency list must be traversed looking for the other vertex, and that list could have V items.
However, in most applications, a vertex is only adjacent to a small fraction of the other verticess, yielding a sparce graph.
A sparse graph has far fewer edges than the maximum possible.
Many graphs are sparse, like those representing a computer network, flights between cities, or friendships among people (every person isn't friends with every other person).
Thus, the adjacency list graph representation is very common.

## Adjacency Matrices:
Various approaches exist for representing a graph data structure.
One approach is an adjacency matrix.
Recall that two vertices are adjacent if connected by an edge.
In an adjacency matrix graph representation, each vertex is assigned to a matrix row and column, and a matrix element is one if the correspondeing two vertices have an edge or is zero otherwise.

### Analysis of Adjacency Matrices:
Assuming the common implementation as a two-dimensional array whose elements are accessible in O(1), then an adjacency matrix's key benefit is O(1) determination of whether two vertices are adjacent.
The corresponding element is just checked for 0 or 1.

A key drawback is O(V<sup>2</sup>) size.
An adjacency matrix's large size is inefficient for a sparse graph, in which most elements would be 0's.

An adjacency matrix only represents edges among vertices; if each vertex has data, then a sepparate list of vertices is needed.

## Breadth-First Search:
An algorithm commonly must visit every vertex in a graph in some order, known as graph traversal.
A breadth-first search (BFS) is a traversal that visits a starting vertex, then all vertices of distance 1 from that vertex, then distance 2, and so on, without revisiting a vertex.

### Breadth-First Search Algorithm:
An algorithm for breadth-first search enqueues the starting vertex in a queue.
While the queue is not empty, the algorithm dequeues a vertex from the queue, visits the dequeued vertex, enqueues that vertex's adjacent vertices (if not already discovered), and repeats.

When the BFS algorithm first encounters a vertex, that vertex is said to have been discovered.
In the BFS algorithm, the vertices in the queue are called the frontier, being vertices thus far discovered but not yet visited.
Because each vertex is visited at most once, an already-discovered vertex is not enqueued again.

A "visit" may mean to print the vertex, append the vertex to a list, compare vertex data to a value and return the vertex if found, etc.

## Depth-First Search:
An algorithm commonly must visit every vertex in a graph in some order, known as graph traversal.
A depth-first search (DFS) is a traversal that visits a starting vertex, then visits every vertex along each path starting from that vertex to the path's end before backtracking.

### Depth-First Search Algorithm:
An algorithm for depth-first search pushes the starting vertex to a stack.
While the stack is not empty, the algorithm pops the vertex from the top of the stack.
If the vertex has not already been visited, the algorithm visits the vertex and pushes the adjacent verticies to the stack.

A recursive DFS can be implemented using the program stack instead of an explicit stack.
The recursive DFS algorithm is first called with the starting vertex.
If the vertex has not already been visited, the recursive algorithm visits the vertex and performs a recursive DFS call for each adjacent vertex.

## Directed Graphs:
A directed graph, or digraph, consists of vertices connected by directed edges.
A directed edge is a connection between a starting vertex and a terminating vertex.
In a directed graph, a vertex Y is adjacent to a vertex X, if there is an edge from X to Y.

Many graphs are directed, like those representing links between web pages, maps for navigation, or college course prerequisites.

In a directed graph:
- A path is a sequence of directed edges leading from a source (starting) vertex to a destination (ending) vertex.
- A cycle is a path that starts sand ends at the same vertex.
A directed graph is cyclic if the graph contains a cycle, and acyclic if the graph does not contain a cycle.

## Weighted Graphs:
A weighted graph associates a weight with each edge.
A graph edge's weight, or cost, represents some numerical value between vertex items, such as flight cost between airports, connection speed between computers, or travel time between cities.
A weighted graph may be directed or undirected.

In a weighted graph, the path length is the sum of the edge weights in the path.

The cycle length is the sum of the edge weights in a cycle.
A negative edge weight cycle has a cycle length less than 0.
A shortest path does not exist in a graph with a negative edge weight cycle, because each loop around the negative edge weight cycle further decreases the cycle length, so no minimum exists.

## Dijkstra's Shortest Path:
Dijkstra's shortest path algorithm, created by Edsger Dijkstra, determines the shortest path from a start vertex to each vertex in a graph.
For each vertex, Dijkstra's algorithm determines the vertex's distance and predecessor pointer.
A vertex's distance is the shortest path distance from the start vertex.
A vertex's predecessor pointer points to the previous vertex along the shortest path from the start vertex.

Dijkstra's algorithm initializes all vertices' distances to infinity (&infin;), initializes all vertices' predecessors to null, and enqueues all vertices into a queue of unvisited vertices.
The algorithm then assigns the start vertex's distance with 0.
Whle the queue is not empty, the algorithm dequeues the vertex with the shortest distance.
For each adjacent vertex, the algorithm computes the distance of the path from the start vertex to the current vertex and continuing on to the adjacent vertex.
If that path's distance is shorter than the adjacent vertex's current distance, a shorter path has been found.
The adjacent vertex's current distance is updated to the distance of the newly found shorter path's distance, and vertex's predecessor pointer is pointed to the current vertex.

After running Dijkstra's algorithm, the shortest path from the start vertex to a destination vertex can be determined using the vertices' predecessor pointers.
If the destination vertex's predecessor pointer is not 0, the shortest path is traversed in reverse by following the predecessor pointers until the start vertex is reached.
If the destination vertex's predecessor pointer is null, then a path from the start vertex to the destination vertex does not exist.

Dijkstra's shortest path algorithm can be used for unweighted graphs (using a uniform edge weight of 1) and weighted graphs with non-negative edges weights.
For a directed graph with negative edge weights, Dijkstra's algorithm may not find the shortest path for some vertices, so the algorithm should not be used if a negative edge weight exists.
