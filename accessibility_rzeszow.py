# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 23:38:34 2020

@author: Kuba
"""

import osmnx as ox
G = ox.graph_from_address('RzeszóW, Poland')
ox.plot_graph(G)

from pandana.loaders import osm

# define your selected amenities and bounding box
amenities = ['hospital', 'clinic', 'restaurant','cafe','school','bank','pharmacy','park']
bbox = [42.325329,-83.047953,42.418919,-83.128327]

# request them from the OpenStreetMap API (Overpass)
pois = osm.node_query(bbox[0], bbox[1], bbox[2], bbox[3],tags=osm_tags)
pois = pois[pois['amenity'].isin(amenities)]

#List how many we downloaded
pois.amenity.value_counts()
pois[['amenity', 'name', 'lat', 'lon']].head()

# initialize each amenity category with the locations (lon/lat coordinates)

for amenity in ['bank','hospital']:
 pois_subset = pois[pois['amenity']==amenity]
 network.set_pois(category=amenity, maxdist = distance, maxitems=num_pois, x_col=pois_subset['lon'], y_col=pois_subset['lat'])
 
 # function to plot distance to selected amenity
 # -- default: distance to nearest amenity
 # -- if a parameter n is supplied, distance to the nth nearest amenity
 
def plot_nearest_amenity(amenity,n):
 accessibility = network.nearest_pois(distance=distance, category=amenity, num_pois=num_pois)
 fig, ax = network.plot(accessibility[n], bbox=bbox)
 ax.set_facecolor('k')
 ax.set_title('Pedestrian accessibility in Rzeszow (Walking distance to {}, meters (n = {}))'.format(amenity,n), fontsize=14);
 
plot_nearest_amenity('school',1)