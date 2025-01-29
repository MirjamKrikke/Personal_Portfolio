# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:13:08 2025

@author: Mirjam Krikke
"""
import geopandas as gpd
import folium
from folium.plugins import MarkerCluster, MeasureControl

"""This code reads a dataset with species and neighborhood data and makes a folium map depicting the count of endagered species in neighborhoods. 
It produces different sized markers for different counts. 
When you click the markers there is a popup with information on the neighborhood, count and breakdown of the different species."""

# Load data
speciesdata = gpd.read_file("Species_Neigborhood_Data.geojson")

# Compute centroids (for markers)
speciesdata["centroid"] = speciesdata.geometry.centroid
speciesdata["latitude"] = speciesdata.centroid.y
speciesdata["longitude"] = speciesdata.centroid.x

# Define color function based on species count
def get_color(species_count):
    if species_count > 200:
        return "green"  
    elif species_count > 100:
        return "yellow"
    elif species_count > 50:
        return "orange"
    else:
        return "red"  

# Create base map
m = folium.Map(location=[speciesdata["latitude"].mean(), speciesdata["longitude"].mean()], zoom_start=10)

# Add Marker Cluster
marker_cluster = MarkerCluster().add_to(m)

# Add markers with colors and size based on species count
for _, row in speciesdata.iterrows():
    popup_html = f"""
    <b>Neighborhood:</b> {row['bu_naam']} ({row['gm_naam']})<br>
    <b>Total Species Count:</b> {row['SUM_TOTAAL']}<br>
    <b>Breakdown:</b><br>
    <b>Bats:</b> {row['SUM_ZOOGDIEREN']}<br>
    <b>Other Mammals:</b> {row['SUM_ZOOGDIERE0']}<br>
    <b>Mollusks:</b> {row['SUM_WEEKDIEREN']}<br>
    <b>Birds:</b> {row['SUM_VOGELS']}<br>
    <b>Fish:</b> {row['SUM_VISSEN']}<br>
    <b>Grasshoppers & Crickets:</b> {row['SUM_SPRINKHANE']}<br>
    <b>Reptiles:</b> {row['SUM_REPTIELEN']}<br>
    <b>Dragonflies:</b> {row['SUM_LIBELLEN']}<br>
    <b>Mayflies & Caddisflies:</b> {row['SUM_HAFTEN_KOK']}<br>
    <b>Butterflies:</b> {row['SUM_DAGVLINDER']}<br>
    <b>Bees & Bumblebees:</b> {row['SUM_BIJEN_EN_H']}<br>
    <b>Amphibians:</b> {row['SUM_AMFIBIEEN']}<br>
    """
    species_popup = folium.Popup(popup_html, max_width=300)

    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=max(3, row["SUM_TOTAAL"]/10),  #Adjust marker size
        color=get_color(row["SUM_TOTAAL"]),
        fill=True,
        fill_color=get_color(row["SUM_TOTAAL"]),
        fill_opacity=0.7,
        popup=species_popup
    ).add_to(marker_cluster)

# Add Scalebar
m.add_child(MeasureControl(primary_length_unit='kilometers'))

# Add Legend 
legend_html = """
<div style="
    position: fixed;
    bottom: 30px;
    left: 30px;
    width: 160px;
    height: auto;
    background: white;
    z-index:9999;
    padding: 10px;
    border-radius: 5px;
    font-size: 14px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
">
<b>Legend</b><br>
<span style="background-color:green; width:10px; height:10px; display:inline-block;"></span> >200 Species<br>
<span style="background-color:yellow; width:10px; height:10px; display:inline-block;"></span> 100-200 Species<br>
<span style="background-color:orange; width:10px; height:10px; display:inline-block;"></span> 50-100 Species<br>
<span style="background-color:red; width:10px; height:10px; display:inline-block;"></span> <50 Species<br>
</div>
"""
m.get_root().html.add_child(folium.Element(legend_html))

# Save and Display Map
m.save("species_clustered_markers.html")
m
