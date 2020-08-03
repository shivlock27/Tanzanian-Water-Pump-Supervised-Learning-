import pandas as pd 
import numpy as np 
import csv

import matplotlib.pyplot as plt 

df1=pd.read_csv("final_data_popcat.csv")
df1=df1.rename(columns={"Unnamed: 0":"Id"})
#print(df1.head())

# Categorical Variables (11) - region, (public_meeting), permit, (extraction_type_group), (management), payment_type, 
#                         quality_group, quantity_group, source_type, waterpoint_type_group, pop_categ 

#==============================================================================
# Region
# df1.groupby(["region", 'status_group']).size().unstack().plot(kind='bar',stacked=True)
# plt.show()
# df1.groupby(["region", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()
#===============================================================================
# public_meeting
# df1.groupby(["public_meeting", 'status_group']).size().unstack().plot(kind='bar',stacked=True)
# plt.show()
# df1.groupby(["public_meeting", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()

#=================================================================================
# permit
# df1.groupby(["permit", 'status_group']).size().unstack().plot(kind='bar',stacked=True)
# plt.show()
# df1.groupby(["permit", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()
#===============================================================================
# extraction_type_group
# df1.groupby(["extraction_type_group", 'status_group']).size().unstack().plot(kind='bar',stacked=True)
# plt.show()
# df1.groupby(["extraction_type_group", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()

#=================================================================================
# management
# df1.groupby(["management", 'status_group']).size().unstack().plot(kind='bar',stacked=True)
# plt.show()
# df1.groupby(["management", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()
#===============================================================================
# payment_type
# df1.groupby(["payment_type", 'status_group']).size().unstack().plot(kind='bar',stacked=True)
# plt.show()
# df1.groupby(["payment_type", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()
#===============================================================================
# quality_group
# df1.groupby(["quality_group", 'status_group']).size().unstack().plot(kind='bar',stacked=True,rot=0)
# plt.show()
# df1.groupby(["quality_group", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()
#===============================================================================
# quantity_group
# df1.groupby(["quantity_group", 'status_group']).size().unstack().plot(kind='bar',stacked=True)
# plt.show()
# df1.groupby(["quantity_group", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()
#===============================================================================
# source_type
# df1.groupby(["source_type", 'status_group']).size().unstack().plot(kind='bar',stacked=True,rot=0)
# plt.show()
# df1.groupby(["source_type", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()
#===============================================================================
# waterpoint_type_group
# df1.groupby(["waterpoint_type_group", 'status_group']).size().unstack().plot(kind='bar',stacked=True,rot=0)
# plt.show()
# df1.groupby(["waterpoint_type_group", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()
#===============================================================================
# pop_categ
# df1.groupby(["pop_categ", 'status_group']).size().unstack().plot(kind='bar',stacked=True)
# plt.show()
# df1.groupby(["pop_categ", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()
#===============================================================================
