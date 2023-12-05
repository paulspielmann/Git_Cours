from collections import deque
import random


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
        return f"Edge between {self.node1} and {self.node2}, {self.weight}"


class Graph:
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

    # Renvoie le poids de l'arrete entre node1 et node2
    def edge_weight(self, node1, node2):
        for edge in self.edges:
            if {edge.node1, edge.node2} == {node1, node2}:
                return edge.weight

    def remove_node(self, node):
        if node in self.nodes:
            del self.nodes[node]
            # Retire toutes les arretes connectees a ce noeud
            self.edges = [edge for edge in self.edges if edge.node1 != node and edge.node2 != node]

            # Update les voisins des autres noeuds du graph
            for n in self.nodes:
                self.nodes[n] = [neighbor for neighbor in self.nodes[n] if neighbor != node]

# Cherche 'target' dans le graph, return true/false
# Peut etre modifie pour faire n'importe quoi qui demande
# de traverser le graph
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
# Parcours le graph depuis start_node et renvoie 2 collections :
# dist -> tableau de distance depuis start_node vers les autres noeuds
# prev -> dictionnaire de la forme (noeud final : liste des noeuds parcourus)
# Ces 2 collections permettent de retrouver le chemin le plus court pour
# arriver a tous les noeuds du tableau
    def dijkstra(self, start_node):
        inf = float('inf')
        queue = set()
        dist = {}
        prev = {}

        for node in self.nodes:
            dist[node] = inf # Toutes les distances sont init a infini
            prev[node] = None
            queue.add(node)

        # La distance vers le noeud de depart est 0 (initialization)
        dist[start_node] = 0

        while queue:
            # Soit u un noeud tq dist[u] est le
            # minimum de tous les noeuds dans la file
            u = min(queue, key=lambda node: dist[node])
            queue.remove(u)

            # On traverse les voisins du u qui sont toujours dans la file
            for n in self.nodes[u]:
                if n in queue:
                    # alt = distance entre start_node et u passant par n
                    alt = dist[u] + self.edge_weight(u, n)
                    if alt < dist[n]:
                        dist[n] = alt
                        prev[n] = u

        return dist, prev


random_graph = Graph()

for i in range(1, 51):
    node = Node(i)
    random_graph.add_node(node)

for _ in range(100):
    node1, node2 = random.sample(list(random_graph.nodes.keys()), 2)
    weight = random.randint(1, 10)
    random_graph.add_edge(node1, node2, weight)

print(random_graph)

print("Random Graph Nodes:")
for node in random_graph.nodes:
    print(node)

print("\nRandom Graph Edges:")
for edge in random_graph.edges:
    print(edge)

# Test BFS
target_node = random.choice(list(random_graph.nodes.keys()))
start_node = random.choice(list(random_graph.nodes.keys()))
print("\nBFS Search on Random Graph with start node ", start_node, " and target node ", target_node, ": ", random_graph.bfs_search(start_node, target_node))

# Test dijkstra
istart_node = random.choice(list(random_graph.nodes.keys()))
distances, predecessors = random_graph.dijkstra(start_node)
print("\nDijkstra Distances from ", start_node, " :")
for node, dist in distances.items():
    print(node, "distance from origin:", dist)

print("\nDijkstra Predecessors:")
for node in predecessors:
    print(f"Predecessor of {node}: {predecessors[node]}")
