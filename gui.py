from tkinter import Tk, Button, Label
from PIL import ImageTk, Image
import geopandas as gpd
import osmnx as ox
import webbrowser
from tkinter import Tk, Button

def plot_route(G, path):
    nodes, edges = ox.graph_to_gdfs(G, nodes=True, edges=True)
    route_nodes = nodes.loc[path]

    m = route_nodes.explore()
    m.save('map.html')


def show_gui():
    root = Tk()
    root.title("Route Visualizer")

    def open_map():
        webbrowser.open("map.html")

    open_button = Button(root, text="Open Map", command=open_map)
    open_button.pack()

    close_button = Button(root, text="Close", command=root.quit)
    close_button.pack()

    root.mainloop()
