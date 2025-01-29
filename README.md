# Background
For this learning goal I initially wanted to make a heatmap of wind energy production for the group project. Because I spend most of my time on preprocessing data, I did not manage to make a nice map for our group project. Therefore I decided to focus a bit more on visualization of the endangered species dataset that I also used for the statistics learning goal. I still liked the idea of a heatmap and I also thought it would be a nice way of displaying species occurrences and hotspots. Therefore I took this idea as a starting point to make some visualizations using folium. I first checked out a heatmap, but for this data there were no real hotspots visible. Especially when zooming into the map the occurrences were all pretty uniform. So I brainstormed on some other ideas to display my data. I decided on making a clustered marker map with the combined species and neighborhood data that I also used for the statistics part. 
# Methodology and Data
To make the folium map I saved my combined species and neighborhood dataset as a geojson. This geojson can also be found in this branch: Species_Neighborhood_Data.geojson. I loaded this into my python script and from the geometry I calculated centroid points for each polygon. These centroids are used as the locations for my markers. I then derived the longitude and latitude of the centroids and used these to initialize my folium map. I then wrote a function to display the markers in different colours for different species counts. After that I added the markers to the map and included the count of all the categories as well as the neighborhood data. At the end of the script I also added some cartographic elements: a legend and scalebar (I also tried to include a north arrow but could not get it right). I then saved and displayed the folium map.
# Results
The resulting folium map will be produced and saved when you run the code. 
# Discussion
The created map nicely shows the different species counts for the different neighborhoods. However, there are still some flaws. I wanted to also add the neighborhood outline of the marker points to the map. I first did this by including all polygons. This resulted in a map that was a bit chaotic, with a lot of neighborhood boundaries the marker points stood out less. I wanted to solve this by only showing the neighborhood outline when a marker was clicked, this would be nice because then you also get a feel about the area of the neighborhood. I spent quite a bit of time working on this but each time it resulted in an empty map even though I got no errors when running the code. I then checked the console of the html for errors and found an error which resulted in the markers not being rendered to the folium map. Very frustrating! I tried fixing this issue, but in the end I just decided to keep the map without the neighborhood outlines. 
Another issue is that the map does not really display new knowledge or information. This is a choice I made. As I wanted to focus on the visualization itself for this learning goal I picked a variable to display that shows some interesting visual differences. I could also have mapped the species density, which takes into account the neighborhood area. But as these showed little variation (which I concluded in the statistics part) I decided not to do this.
What I do like about the visualization is that it enables you to look into different neighborhoods to find out the endagered species count. In my neighborhood there were not so many, but for an urban area it could be worse. If there were clear hotspots this would be valuable information for biodiversity conservation. 
# Reflection on learning goal
I think I managed to make a nice interactive visualization in folium, albeit not a heatmap. I really liked working on this learning goal in the end as I think data visualization is really cool! By looking into different visualization types and just trying things out, I learnt a lot about which kinds of visualizations work for different data types. At the start of this course I already felt quite comfortable with visualizing data in arcGIS, so I think that doing the visualization using folium was a nice challenge. During geoscripting some of my groupmembers already used this to create interactive maps, which inspired me to try it for myself. I think this package is great for making interactive maps rather than static maps using arcGIS. As mentioned in the discussion, there is still some room for improvement. For future projects I think it could also be nice to make a map layer in Google Maps if there is a navigation aspect to the project. I did really enjoy the biodiversity topic of this visualization. This is something I would like to focus on more during other courses. 
