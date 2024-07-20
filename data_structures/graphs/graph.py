'''
    Graph
    -----
'''
from ..stacks_and_queues.queue import Queue
from typing import List

class Graph:
    class Vertex:
        def __init__(self, label):
            self.label = label
            self.distance = float('inf')
            self.pred_vertex = None

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

    # Breadth-first search function.
    def breadth_first_search(graph, start_vertex: Vertex, distances=dict()):
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
    def depth_first_search(graph, start_vertex: Vertex, visit_function):
        vertex_stack = [start_vertex]
        visited_set = set()
        while len(vertex_stack) > 0:
            current_vertex = vertex_stack.pop()
            if current_vertex not in visited_set:
                visit_function(current_vertex)
                visited_set.add(current_vertex)
                for adjacent_vertex in graph.adjacency_list[current_vertex]:
                    vertex_stack.append(adjacent_vertex)

    def dijkstra_shortes_path(g, start_vertex: Vertex):
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
