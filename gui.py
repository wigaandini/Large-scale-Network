from tkinter import Tk, Button, Label, Entry
import geopandas as gpd
import osmnx as ox
import webbrowser

def plot_route(G, path):
    nodes, edges = ox.graph_to_gdfs(G, nodes=True, edges=True)
    route_nodes = nodes.loc[path]
    m = route_nodes.explore()
    m.save('map.html')

def show_gui(process_route_callback):
    root = Tk()
    root.title("Route Network")
    root.geometry('500x320') 
    bg_color = '#f9dced'

    root.configure(bg=bg_color)

    Label(root, text="City:", bg=bg_color, fg='black').pack(pady=(10, 0))
    city_entry = Entry(root)
    city_entry.pack(pady=(0, 10))

    Label(root, text="Start Address:", bg=bg_color, fg='black').pack(pady=(10, 0))
    start_entry = Entry(root)
    start_entry.pack(pady=(0, 10))

    Label(root, text="End Address:", bg=bg_color, fg='black').pack(pady=(10, 0))
    end_entry = Entry(root)
    end_entry.pack(pady=(0, 10))

    def on_submit():
        city = city_entry.get()
        start_addr = start_entry.get()
        end_addr = end_entry.get()
        process_route_callback(city, start_addr, end_addr)
        open_map()  

    submit_button = Button(root, text="Find Route", bg='#d6aec6', command=on_submit)
    submit_button.pack(pady=(10, 5))

    def open_map():
        webbrowser.open("map.html")

    close_button = Button(root, text="Close", bg='#d6aec6', command=root.quit)
    close_button.pack(pady=(5, 10))

    root.mainloop()
