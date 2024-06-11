import networkx as nx
import osmnx as ox

def heuristic(node1, node2, G):
    return ox.distance.euclidean(G.nodes[node1]['y'], G.nodes[node1]['x'], G.nodes[node2]['y'], G.nodes[node2]['x'])


def astar(G, start, goal):
    return nx.astar_path(G, start, goal, heuristic=lambda n1, n2: heuristic(n1, n2, G), weight='length')
