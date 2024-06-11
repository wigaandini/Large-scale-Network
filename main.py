from data import download_road
from astar import astar
from gui import plot_route, show_gui
import osmnx as ox

def main():
    city = 'Bandung, Indonesia'
    G = download_road(city)
    
    start_addr = "Jalan Asia Afrika, Bandung"
    end_addr = "Bandung Institute of Technology, Bandung"

    start_node = ox.distance.nearest_nodes(G, ox.geocoder.geocode(start_addr)[1], ox.geocoder.geocode(start_addr)[0])
    end_node = ox.distance.nearest_nodes(G, ox.geocoder.geocode(end_addr)[1], ox.geocoder.geocode(end_addr)[0])
    
    path = astar(G, start_node, end_node)
    plot_route(G, path)
    show_gui()

if __name__ == "__main__":
    main()
