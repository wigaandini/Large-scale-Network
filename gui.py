from tkinter import Tk, Button, Label, Entry, StringVar
import geopandas as gpd
import osmnx as ox
import webbrowser
import time

def plot_route(G, path):
    nodes, edges = ox.graph_to_gdfs(G, nodes=True, edges=True)
    route_nodes = nodes.loc[path]
    m = route_nodes.explore()
    m.save('map.html')

def show_gui(process_route_callback):
    root = Tk()
    root.title("Route Network")
    root.geometry('500x310') 
    bg_color = '#f9dced'

    root.configure(bg=bg_color)

    time_var = StringVar()
    # time_var.set("Execution Time: 0 seconds")

    Label(root, text="City:", bg=bg_color, fg='black').pack(pady=(10, 0))
    city_entry = Entry(root, width=50)
    city_entry.pack(pady=(0, 10))

    Label(root, text="Start Address:", bg=bg_color, fg='black').pack(pady=(10, 0))
    start_entry = Entry(root, width=50)
    start_entry.pack(pady=(0, 10))

    Label(root, text="End Address:", bg=bg_color, fg='black').pack(pady=(10, 0))
    end_entry = Entry(root, width=50)
    end_entry.pack(pady=(0, 10))

    def on_submit():
        city = city_entry.get()
        start_addr = start_entry.get()
        end_addr = end_entry.get()
        exec_time = process_route_callback(city, start_addr, end_addr)
        time_var.set(f"Execution Time: {exec_time:.2f} seconds")
        open_map()  

    submit_button = Button(root, text="Find Route", bg='#d6aec6', command=on_submit)
    submit_button.pack(pady=(10, 5))

    exec_time_label = Label(root, textvariable=time_var, bg=bg_color, fg='black')
    exec_time_label.pack()

    def open_map():
        webbrowser.open("map.html")

    close_button = Button(root, text="Close", bg='#d6aec6', command=root.quit)
    close_button.pack(pady=(5, 10))

    root.mainloop()
