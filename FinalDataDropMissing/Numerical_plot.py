# https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51
import pandas as pd 
import numpy as np 
import csv

import matplotlib.pyplot as plt 

df1=pd.read_csv("final_data_popcat.csv")
df1=df1.rename(columns={"Unnamed: 0":"Id"})
#print(df1.head())

# Numerical Variables (3) - 'gps_height','population','construction_age'  

#===========================================================================
# gps_height
# df1.boxplot(by="status_group",column=["gps_height"],grid=False)
# plt.show()

#============================================================================
# # population
# df1.boxplot(by="status_group",column=["population"],grid=False,rot=0)
# plt.show()

#============================================================================
# construction_age
# df1.boxplot(by="status_group",column=["construction_age"],grid=False)
# plt.show()

#============================================================================
