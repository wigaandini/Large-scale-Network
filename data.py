import osmnx as ox

def download_road_network(city_name):
    G = ox.graph_from_place(city_name, network_type='drive')
    return G
