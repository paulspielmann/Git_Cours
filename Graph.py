from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __str__(self):
        return f"Node {self.value}"


class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight

    def __str__(self):
        return f"Edge between {node1} and {node2}, {self.weight}"


class Graph:
    # Adjacency : 2 nodes are adjacent
    # if they are connected by an edge
    # Adjacency list :
    # Dictionnary where each key is a Node and the value associated
    # with that Node is a list of neihgbors
    # Better for smaller graphs, O(n+e) space where n,e is nb of nodes,edges

    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []

    def add_edge(self, node1, node2, weight):
        if node1 in self.nodes and node2 in self.nodes:
            self.nodes[node1].append(node2)
            self.nodes[node2].append(node1)
            self.edges.append(Edge(node1, node2, weight))

    # Returns the weight of the edge between nodes 1 and 2
    def edge_weight(self, node1, node2):
        for edge in self.edges:
            if {edge.node1, edge.node2} == {node1, node2}:
                return edge.weight

# Currently this searches for 'target' value in the graph, but this can
# do pretty much anything that requires traversing the graph.
    def bfs_search(self, start_node, target):
        visited = set()
        queue = deque([start_node])

        while queue:
            current_node = queue.popleft()
            if current_node.value == target:
                return True

            if current_node not in visited:
                visited.add(current_node)

            queue.extend(neighbor for neighbor in current_node.neighbors if neighbor not in visited)
        return False

# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
# dist is an array of distance from source to other nodes
# prev is an array of previous hop-nodes on the shortest path to current node
    def dijkstra(self, start_node):
        inf = float('inf')
        queue = set()
        dist = {}
        prev = {}

        for node in self.nodes:
            dist[node] = inf
            prev[node] = None
            queue.add(node)

        # Distance from start node to current node is 0
        dist[start_node] = 0

        while queue:
            # Let u be a Node, find u such as dist[u]
            # is the min out of all nodes in the queue
            u = min(queue, key=lambda node: dist[node])
            queue.remove(u)

            # Go through u's neighbors that are still in the queue
            for n in self.nodes[u]:
                if n in queue:
                    # alt = distance from root to n through u
                    alt = dist[u] + self.edge_weight(u, n)
                    if alt < dist[n]:
                        dist[n] = alt
                        prev[n] = u

        return dist, prev


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

graph = Graph()
graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)
graph.add_node(node4)
graph.add_node(node5)

graph.add_edge(node1, node2, 1)
graph.add_edge(node2, node3, 2)
graph.add_edge(node3, node4, 3)
graph.add_edge(node4, node5, 4)
graph.add_edge(node5, node1, 5)

# Test BFS search
print("BFS Search:", graph.bfs_search(node1, 3))  # Should print True

# Test Dijkstra's algorithm
distances, predecessors = graph.dijkstra(node1)
print("Dijkstra Distances:")
for node, dist in distances.items():
    print(node, "distance a l'origine", dist)

print("Dijkstra Predecessors:")
for node in predecessors:
    print(node)
