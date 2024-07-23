'''
    Graph
    -----
'''
from ..stacks_and_queues.queue import Queue
from typing import List
import heapq

class Graph:
    class Vertex:
        def __init__(self, label):
            self.label = label
            self.distance = float('inf')
            self.pred_vertex: Graph.Vertex = None

    class EdgeWeight:
        def __init__(self, from_vertex, to_vertex, weight):
            self.from_vertex: Graph.Vertex = from_vertex
            self.to_vertex: Graph.Vertex = to_vertex
            self.weight: float = weight

        # Only edge weights are used in the comparisons below.
        def __eq__(self, other: 'Graph.EdgeWeight'):
            return self.weight == other.weight

        def __ge__(self, other: 'Graph.EdgeWeight'):
            return self.weight >= other.weight

        def __gt__(self, other: 'Graph.EdgeWeight'):
            return self.weight > other.weight

        def __le__(self, other: 'Graph.EdgeWeight'):
            return self.weight <= other.weight

        def __lt__(self, other: 'Graph.EdgeWeight'):
            return self.weight < other.weight

        def __ne__(self, other: 'Graph.EdgeWeight'):
            return self.weight != other.weight

    # Stores a collection of vertex sets, which collectively store all vertices in a graph.
    # Each vertex is in only one set in the collection.
    class VertexSetCollection:
        def __init__(self, all_vertices: List['Graph.Vertex']):
            self.vertex_map = dict()
            for vertex in all_vertices:
                vertex_set = set()
                vertex_set.add(vertex)
                self.vertex_map[vertex] = vertex_set

        def __len__(self):
            return len(self.vertex_map)

        # Gets the set containing the specified vertex.
        def get_set(self, vertex: 'Graph.Vertex'):
            return self.vertex_map[vertex]

        # Merges two vertex sets into one.
        def merge(self, vertex_set1: set, vertex_set2: set):
            # First create the union.
            merged = vertex_set1.union(vertex_set2)
            # Now remap all vertices in the merged set.
            for vertex in merged:
                self.vertex_map[vertex] = merged

    def __init__(self):
        self.adjacency_list: dict = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex: Vertex):
        self.adjacency_list[new_vertex] = []

    def add_directed_edge(self, from_vertex: Vertex, to_vertex: Vertex, weight: float = 1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex] = to_vertex

    def add_undirected_edge(self, vertex_a: Vertex, vertex_b: Vertex, weight: float = 1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    # Returns the vertex in this graph with the specified label, or None if no such vertex exists.
    def get_vertex(self, vertex_label):
        for vertex in self.adjacency_list:
            vertex: Graph.Vertex
            if vertex.label == vertex_label:
                return vertex
        return None

    # Returns a list of all vertices in this graph.
    def get_vertex_list(self):
        return list(self.adjacency_list)

    # Returns a list of all edges incoming to the specified vertex.
    # Each edge is a tuple of the form (from_vertex, to_vertex).
    def get_incoming_edges(self, vertex: Vertex):
        incoming = []
        for edge in self.edge_weights:
            if edge[1] is vertex:
                incoming.append(edge)
        return incoming

    # Breadth-first search function.
    def breadth_first_search(graph: 'Graph', start_vertex: Vertex, distances=dict()):
        discovered_set = set()
        frontier_queue: Queue = Queue()
        visited_list = []
        # Start vertex has a distance of 0 from itself.
        distances[start_vertex] = 0
        # Enqueue start_vertex in frontier_queue.
        frontier_queue.enqueue(start_vertex)
        # Add start_vertex to discovered_set.
        discovered_set.add(start_vertex)
        while (frontier_queue.list.head != None):
            current_vertex = frontier_queue.dequeue()
            visited_list.append(current_vertex)
            for adjacent_vertex in graph.adjacency_list[current_vertex]:
                if adjacent_vertex not in discovered_set:
                    frontier_queue.enqueue(adjacent_vertex)
                    discovered_set.add(adjacent_vertex)
                    # Distance of adjacent_vertex is 1 more than current_vertex.
                    distances[adjacent_vertex] = distances[current_vertex] + 1
        return visited_list

    # Depth-first search function.
    def depth_first_search(graph: 'Graph', start_vertex: Vertex, visit_function):
        vertex_stack = [start_vertex]
        visited_set = set()
        while len(vertex_stack) > 0:
            current_vertex = vertex_stack.pop()
            if current_vertex not in visited_set:
                visit_function(current_vertex)
                visited_set.add(current_vertex)
                for adjacent_vertex in graph.adjacency_list[current_vertex]:
                    vertex_stack.append(adjacent_vertex)

    def dijkstra_shortes_path(g: 'Graph', start_vertex: Vertex):
        # Put all vertices in an unvisited queue.
        unvisited_queue: List[Graph.Vertex] = []
        for current_vertex in g.adjacency_list:
            unvisited_queue.append(current_vertex)
        # start_vertex has a distance of 0 from itself.
        start_vertex.distance = 0
        # One vertex is removed with each iteration; repeat until the list is empty.
        while len(unvisited_queue) > 0:
            # Visit vertex with minimum distance from start_vertex.
            smallest_index = 0
            for i in range(1, len(unvisited_queue)):
                if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                    smallest_index = i
            current_vertex: Graph.Vertex = unvisited_queue.pop(smallest_index)
            # Check potential path legths from the current vertex to all neighbors.
            for adj_vertex in g.adjacency_list[current_vertex]:
                adj_vertex: Graph.Vertex
                edge_weight = g.edge_weights[(current_vertex, adj_vertex)]
                alternative_path_distance = current_vertex.distance + edge_weight
                # If shorter path from start_vertex to adj_vertex is found, update adj_vertex's distance and predecessor.
                if alternative_path_distance < adj_vertex.distance:
                    adj_vertex.distance = alternative_path_distance
                    adj_vertex.pred_vertex = current_vertex

    def get_shortest_path(start_vertex: Vertex, end_vertex: Vertex):
        # Start from end_vertex and build the path backwards.
        path = ''
        current_vertex = end_vertex
        while current_vertex is not start_vertex:
            path = ' -> ' + str(current_vertex.label) + path
            current_vertex = current_vertex.pred_vertex
        path = start_vertex.label + path
        return path

    def bellman_ford(graph: 'Graph', start_vertex: Vertex):
        # Initialize all vertex distances to infinity and predecessor verticies to None.
        for current_vertex in graph.adjacency_list:
            current_vertex: Graph.Vertex
            current_vertex.distance = float('inf')
            current_vertex.pred_vertex = None
        # start_vertex has a distance of 0 from itself.
        start_vertex.distance = 0
        # Main loop is executed |V| - 1 times to guarantee minimum distances.
        for i in range(len(graph.adjacency_list) - 1):
            # Main loop.
            for current_vertex in graph.adjacency_list:
                current_vertex: Graph.Vertex
                for adj_vertex in graph.adjacency_list[current_vertex]:
                    adj_vertex: Graph.Vertex
                    edge_weight = graph.edge_weights[(current_vertex, adj_vertex)]
                    alternative_path_distance = current_vertex.distance + edge_weight
                    # If shorter path from start_vertex to adj_vertex is found, update adj_vertex's distance and predecessor.
                    if alternative_path_distance < adj_vertex.distance:
                        adj_vertex.distance = alternative_path_distance
                        adj_vertex.pred_vertex = current_vertex
        # Check for a negative edge weight cycle.
        for current_vertex in graph.adjacency_list:
            current_vertex: Graph.Vertex
            for adj_vertex in graph.adjacency_list[current_vertex]:
                adj_vertex: Graph.Vertex
                edge_weight = graph.edge_weights[(current_vertex, adj_vertex)]
                alternative_path_distance = current_vertex.distance + edge_weight
                # If shorter path from start_vertex to adj_vertex is still found, a negative edge weight cycle exists.
                if alternative_path_distance < adj_vertex.distance:
                    return False
        return True

    def get_incoming_edge_count(edge_list, vertex: Vertex):
        count = 0
        for (from_vertex, to_vertex) in edge_list:
            if to_vertex is vertex:
                count = count + 1
        return count

    def topological_sort(self, graph: 'Graph'):
        result_list = []
        # Make list of vertices with no incoming edges.
        no_incoming = []
        for vertex in graph.adjacency_list.keys():
            if self.get_incoming_edge_count(graph.edge_weights.keys(), vertex=vertex) == 0:
                no_incoming.append(vertex)
        # remaining_edges starts with all edges in the graph.
        # A set is used for its efficient remove() method.
        remaining_edges = set(graph.edge_weights.keys())
        while len(no_incoming) != 0:
            # Select the next vertex for the final result.
            current_vertex = no_incoming.pop()
            result_list.append(current_vertex)
            # Remove current vertex's outgoing edges from remaining_edges.
            outgoing_edges = []
            for to_vertex in graph.adjacency_list[current_vertex]:
                outgoing_edge = (current_vertex, to_vertex)
                if outgoing_edge in remaining_edges:
                    outgoing_edges.append(outgoing_edge)
                    remaining_edges.remove(outgoing_edge)
            # See if removing the outgoing edges creates any new vertices with no incoming edges.
            for (from_vertex, to_vertex) in outgoing_edges:
                in_count = self.get_incoming_edge_count(remaining_edges, to_vertex)
                if in_count == 0:
                    no_incoming.append(to_vertex)
        return result_list

    # Returns a list of edges representing the graph's minimum spanning tree.
    # Uses Kruskal's minimum spanning tree algorithm.
    def minimum_spanning_tree(graph: 'Graph'):
        # edge_list starts as a list of all edges from the graph.
        edge_list = []
        for edge in graph.edge_weights:
            edge_weight = Graph.EdgeWeight(edge[0], edge[1], graph.edge_weights[edge])
            edge_list.append(edge_weight)
        # Turn edge_list into a priority queue (min heap).
        heapq.heapify(edge_list)
        # Initialize the collection of vertex sets.
        vertex_sets = Graph.VertexSetCollection(graph.adjacency_list)
        # result_list is initially an empty list.
        result_list = []
        while len(vertex_sets) > 1 and len(edge_list) > 0:
            # Remove edge with minimum weight from edge_list.
            next_edge: Graph.EdgeWeight = heapq.heappop(edge_list)
            # Set1 = set in vertex_sets containing next_edge's 'from' vertex.
            set1 = vertex_sets.get_set(next_edge.from_vertex)
            # Set2 = set in vertex_sets containing next_edge's 'to' vertex.
            set2 = vertex_sets.get_set(next_edge.to_vertex)
            # If the two sets are distinct, then merge.
            if set1 is not set2:
                # Add next_edge to result_list.
                result_list.append(next_edge)
                # Merge the two sets within the collection.
                vertex_sets.merge(set1, set2)
        return result_list

    # Implementation of Floyd-Warshall all-pairs shortest path.
    def all_pairs_shortest_path(graph: 'Graph'):
        vertices = graph.get_vertex_list()
        num_vertices = len(vertices)
        # Initializes dist_matrix to a num_vertices x num_vertices matrix with all values set to infinity.
        dist_matrix = []
        for i in range(0, num_vertices):
            dist_matrix.append([float('inf')] * num_vertices)
        # Set each distance for vertex to same vertex to 0.
        for i in range(0, num_vertices):
            dist_matrix[i][i] = 0
        # Finish matrix initialization.
        for edge in graph.edge_weights:
            dist_matrix[vertices.index(edge[0])][vertices.index(edge[1])] = graph.edge_weights[edge]
        # Loop through vertices.
        for k in range(0, num_vertices):
            for toIndex in range(0, num_vertices):
                for fromIndex in range(0, num_vertices):
                    currentLength = dist_matrix[fromIndex][toIndex]
                    possibleLength = dist_matrix[fromIndex][k] + dist_matrix[k][toIndex]
                    if possibleLength < currentLength:
                        dist_matrix[fromIndex][toIndex] = possibleLength
        return dist_matrix

    def reconstruct_path(graph: 'Graph', start_vertex: Vertex, end_vertex: Vertex, dist_matrix):
        vertices = graph.get_vertex_list()
        start_index = vertices.index(start_vertex)
        path = []
        # Backtrack from the ending vertex.
        current_index = vertices.index(end_vertex)
        while current_index != start_vertex:
            incoming_edges = graph.get_incoming_edges(vertices[current_index])
            found_next = False
            for current_edge in incoming_edges:
                expected = dist_matrix[start_index][current_index] - graph.edge_weights[current_edge]
                actual = dist_matrix[start_index][vertices.index(current_edge[0])]
                if expected == actual:
                    # Update current vertex index.
                    current_index = vertices.index(current_edge[0])
                    # Prepend current edge to path.
                    path = [current_edge] + path
                    # The next vertex in the path was found.
                    found_next = True
                    # The correct incoming edge was found, so break the inner loop.
                    break
            if found_next == False:
                # No path exists.
                return None
        return path
