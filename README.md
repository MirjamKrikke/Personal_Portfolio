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
