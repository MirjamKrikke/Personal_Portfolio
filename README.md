# Statistical Analysis
## Background
During the group project I did not manage to do a lot of statistics. Therefore, I decided to do some data statistics on a new project after the group project was finished. I wanted to do a project with some biodiversity data. For this I found a dataset with endangered fauna species in the province of Utrecht. These are species that are on the red list of IUCN. I wanted to look into the relationship between occurrences of endangered species and population density. For this I also loaded neighborhood census data from CBS.
## Data Sources
Red list fauna species dataset: https://www.nationaalgeoregister.nl/geonetwork/srv/dut/catalog.search#/metadata/07c3e3f5-bf56-4888-b8fa-537d6afa1983
CBS neighborhood census data: Ihttps://www.arcgis.com/home/item.html?id=67baac160a51405e875f1686a04d6db8 (I found this through the living atlas portal in arcGIS)
## Methodology
I started with preprocessing my data in arcGIS. I first combined the species data with the CBS data, for this I did an intersect. I then aggregated the features based on population density, neighborhood name and municipality name while also including the total number of each species as well as the total occurrences. I then calculated the species density by dividing the total occurrences in each neighborhood by the area in km2. I then exported this to a csv file for further analysis in Python. 
In the Python script I calculate some statistics to see if there is a correlation between species density and population density. This includes a calculating correlation, making a scatterplot, a regression analysis and a regression plot. This script can also be found in this branch: SpeciesAnalysis.py
The csv file which I used in this script can also be found in this branch: SpeciesAndNeighborhoodData.csv
## Results
The results can be found as pictures in this branch.
Correlation graph: Correlation_graph.png
Regression: Regression_graph.png
Print screen of correlation coefficients and regression analysis: Model_output.JPG
## Conclusion
As the regression coefficient is -0.01. There is no correlation between species density and population density for my dataset. This could have to do with the nature of the data. For data on endangered species you do not expect high numbers of occurrences. This was generally the case, there where some high numbers in rural areas which were very big, resulting in a low species density. For neighborhoods within the cities there could be a relatively high species density. This is because these neighborhoods are generally small in size and thus a few occurrences already result in a relatively high species density. 

## Reflection on the learning goal
During this course I learned to do some statistics using Python. During the group project and in the species project I did some basic statistics, to see if there is a correlation between two variables. This is not very complex but it can be very insightful. However, this type of statistics is so basic that I don't think I really learned a lot about statistics. The skills I gained are more related to the scripting part, which is quite straightforward. So this learning goal is still very relevant for me and I want to develop myself further in this in other courses. Especially the course on spatial modelling and statistics will hopefully bring me new statistical knowledge. 
