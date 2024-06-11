from data import download_road_network
from astar import a_star_algorithm
from gui import plot_route, show_gui
import osmnx as ox

def main():
    city_name = 'Bandung, Indonesia'
    G = download_road_network(city_name)
    
    start_addr = "Jalan Sukajadi, Bandung"
    end_addr = "Bandung Institute of Technology, Bandung"

    start_node = ox.distance.nearest_nodes(G, ox.geocoder.geocode(start_addr)[1], ox.geocoder.geocode(start_addr)[0])
    end_node = ox.distance.nearest_nodes(G, ox.geocoder.geocode(end_addr)[1], ox.geocoder.geocode(end_addr)[0])
    
    path = a_star_algorithm(G, start_node, end_node)
    plot_route(G, path)
    show_gui()

if __name__ == "__main__":
    main()
