# Personal Portfolio
## Introdction
In this repository I reflect on my personal learning goals for the course Data Science for Smart Environments. I will start by summarizing the learning goals that I set at the start of this course. For each learning goal I will then show how I worked on this goal during the group project as well as outside the project where suitable. For each learning goal I will reflect on the methodology and data sources, implementation, results and conclusions.

## Original Learning Goals
1. Visualization: For this learning goal I wanted to implement a new visualization technique in the group project. An idea about the type of visualization was to make a heatmap using the python Folium package or arcGIS.
2. Time management: For this goal I wanted to keep track of time in our project by making a weekly planning and setting clear and concrete goals.
3. Statistical data analysis: For this goal I wanted to learn more about data analysis and statistics and learning new statistical methods.
4. My role in data science: For this goal I wanted to reflect on my role in data science and how it aligns with my academic interests.

## Group Project
During the group project my group focussed on wind energy production in the Netherlands. We derived and compared the amount of wind energy produced per turbine from a weather model as well as from weather station measurements. Deliverables were some plots of energy production over time as well as some regression plots, covariance matrices and a principal components analysis. During this project I maily focussed on the data collection and processing. In the end I also managed to produce some plots. 
### Methodology
I found datasets for the locations of wind turbines as well as the locations and measurements from weather stations. Another team member downloaded data derived from the model (both location and measurements). We first matched the model location data to the wind turbine location data from which we selected a set of wind turbines for analysis. I then matched these selected wind turbines to the weather station location data and measurements. This step took a lot of time as I first matched the weather stations to the selected turbines incorrectly resulting in all weather stations being used, while in reality some weather stations were not closest to any turbine and would therefore be irrelevant while some weather stations would be matched to multiple turbines. The phase in which the location data on both selected turbines and weather stations was then matched to the actual measurements at those weather stations was then very difficult as measurements at one weather station could not be joined to multiple turbines, leaving us with only a limited set of turbines. 
### What went well

# Background
During the group project I did not manage to do a lot of statistics. Therefore, I decided to do some data statistics on a new project after the group project was finished. I wanted to do a project with some biodiversity data. For this I found a dataset with endangered fauna species in the province of Utrecht. These are species that are on the red list of IUCN. I wanted to look into the relationship between occurrences of endangered species and population density. For this I also loaded neighborhood census data from CBS.
# Data Sources
Red list fauna species dataset: https://www.nationaalgeoregister.nl/geonetwork/srv/dut/catalog.search#/metadata/07c3e3f5-bf56-4888-b8fa-537d6afa1983
CBS neighborhood census data: Ihttps://www.arcgis.com/home/item.html?id=67baac160a51405e875f1686a04d6db8 (I found this through the living atlas portal in arcGIS)
# Methodology
I started with preprocessing my data in arcGIS. I first combined the species data with the CBS data, for this I did an intersect. I then aggregated the features based on population density, neighborhood name and municipality name while also including the total number of each species as well as the total occurrences. I then calculated the species density by dividing the total occurrences in each neighborhood by the area in km2. I then exported this to a csv file for further analysis in Python. 
In the Python script I calculate some statistics to see if there is a correlation between species density and population density. This includes a calculating correlation, making a scatterplot, a regression analysis and a regression plot. This script can also be found in this branch: SpeciesAnalysis.py
The csv file which I used in this script can also be found in this branch: SpeciesAndNeighborhoodData.csv
# Results
The results can be found as pictures in this branch.
Correlation graph: Correlation_graph.png
Regression: Regression_graph.png
Print screen of correlation coefficients and regression analysis: Model_output.JPG
# Conclusion
As the regression coefficient is -0.01. There is no correlation between species density and population density for my dataset. This could have to do with the nature of the data. For data on endangered species you do not expect high numbers of occurrences. This was generally the case, there where some high numbers in rural areas which were very big, resulting in a low species density. For neighborhoods within the cities there could be a relatively high species density. This is because these neighborhoods are generally small in size and thus a few occurrences already result in a relatively high species density. 

