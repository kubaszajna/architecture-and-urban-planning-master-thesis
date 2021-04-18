# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:52:45 2020

@author: Kuba
"""


import folium
import pandas as pd 
import numpy as np  
import osmnx as ox
import networkx as nx
import os

ox.config(use_cache=True, log_console=True)

G = ox.graph_from_point((42.331429, -83.045753), dist=1000, network_type='drive')

G = ox.speed.add_edge_speeds(G)
G = ox.speed.add_edge_travel_times(G)

orig = ox.get_nearest_node(G, (42.3319, -83.0170))
dest = ox.get_nearest_node(G, (42.3469, -83.0330))
route = nx.shortest_path(G, orig, dest, 'travel_time')

route_map = ox.plot_route_folium(G, route)
route_map.save('route_334.html')