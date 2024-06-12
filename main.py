from data import download_road
from astar import astar
from gui import plot_route, show_gui
import osmnx as ox
import time

def process_route(city, start_addr, end_addr):
    start_time = time.time()
    G = download_road(city)
    start_node = ox.distance.nearest_nodes(G, ox.geocoder.geocode(start_addr)[1], ox.geocoder.geocode(start_addr)[0])
    end_node = ox.distance.nearest_nodes(G, ox.geocoder.geocode(end_addr)[1], ox.geocoder.geocode(end_addr)[0])
    path = astar(G, start_node, end_node)
    plot_route(G, path)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def main():
    show_gui(process_route)

if __name__ == "__main__":
    main()
