import pandas as pd 
import numpy as np 
import csv

import matplotlib.pyplot as plt 

# df=pd.read_csv("final_data_popcut.csv")
# df=df.rename(columns={"Unnamed: 0":"Id"})
# print(df.head())


#=============================================================================
# Column 19 - Population
# Can't determine whether categorical or numerical
# Even if we take it as categorical, we have to combine values to make new categories
# print(len(df["population"].unique()))   # 1049
# print(len(df[df["population"]==0]))     # 21k entries with 0 population
# print(df["population"].max())			# 30500
# print(df["population"].mean())			# 180
# print(df["population"].min())			# 0
# ans_dict={}
# for i in df["population"]:
# 	if i in ans_dict.keys():
# 		ans_dict[i]+=1
# 	else:
# 		ans_dict[i]=1
# #print(ans_dict)          # For all unique values of population, the number of times it occurs
# #print(ans_dict.values())
# f=open("population.csv","w")
# header=("population,Count")
# f.write(header+"\n")
# for elem in ans_dict.keys():
# 	cs="{},{}".format(elem,ans_dict[elem])
# 	f.write(cs+"\n")
# f.close()


# =========================================================

#print(df["population"].describe())
# count    26534.000000
# mean       250.394890
# std        521.676478
# min          0.000000

# 25%         21.250000
# 50%        130.000000
# 75%        300.000000

# max      30500.000000


#===========================================================

#print(pd.qcut(df["population"],q=4))
# bin_labels=['First','Second','Third','Fourth']
# df["pop_categ"]=pd.qcut(df["population"],q=4,labels=bin_labels)  # Cut the data based on percentiles

# print(df["pop_categ"].value_counts())
# (130.0, 300.0]      7005   Third
# (21.25, 130.0]      6763   Second
# (-0.001, 21.25]     6634   First
# (300.0, 30500.0]    6132   Fourth

#print(df.head())

# df.to_csv("final_data_popcat.csv")



#==============================================================

