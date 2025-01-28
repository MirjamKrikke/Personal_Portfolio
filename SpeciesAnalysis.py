# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 13:30:32 2025

@author: Mirjam Krikke
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, pearsonr
import statsmodels.api as sm 

# Load species data
species = pd.read_csv('SpeciesAndNeighborhoodData.csv')

# Replace nan values for population density with 0
species['bev_dichth'] = species['bev_dichth'].fillna(0)

### Correlation Analysis ###
# Pearson Correlation (linear relationship)
pearson_corr, pearson_p = pearsonr(species['SpeciesDensity'], species['bev_dichth'])
print(f"Pearson Correlation: {pearson_corr:.2f}, P-value: {pearson_p:.3e}")

# Spearman Correlation (monotonic relationship)
spearman_corr, spearman_p = spearmanr(species['SpeciesDensity'], species['bev_dichth'])
print(f"Spearman Correlation: {spearman_corr:.2f}, P-value: {spearman_p:.3e}")

### Scatter Plot ###
sns.scatterplot(data=species, x='bev_dichth', y='SpeciesDensity')
plt.yscale("log")
plt.xscale("log")
plt.title("Species Density vs Population Density")
plt.xlabel("Population Density")
plt.ylabel("Species Density")
plt.show()

### Regression Analysis ###
# Define the independent (X) and dependent (Y) variables
X = species['bev_dichth']   
Y = species['SpeciesDensity']      

# Add a constant to the model (intercept)
X = sm.add_constant(X)

# Fit an Ordinary Least Squares (OLS) regression model
model = sm.OLS(Y, X).fit()

# Print the regression results
print(model.summary())

### Regression Plot ###
sns.regplot(data=species, x='bev_dichth', y='SpeciesDensity', ci=95, line_kws={"color": "red"})
plt.yscale("log")
plt.xscale("log")
plt.title("Regression: Species Density vs Population Density")
plt.xlabel("Population Density")
plt.ylabel("Species Density")
plt.show()
