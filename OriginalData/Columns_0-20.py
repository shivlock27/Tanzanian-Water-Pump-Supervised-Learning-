# Resources for other references
# https://rstudio-pubs-static.s3.amazonaws.com/339668_006f4906390e41cea23b3b786cc0230a.html
# http://courseprojects.souravsengupta.com/cds2016/tanzanias-water-problem-pump-it-up/
# https://joomik.github.io/waterpumps/
# https://joomik.carto.com/builder/3227f55e-d6ac-11e6-832f-0e3ebc282e83/embed?state=%7B%22map%22%3A%7B%22ne%22%3A%5B-13.26561074048497%2C21.49804808199406%5D%2C%22sw%22%3A%5B1.3358161991064008%2C50.589844956994064%5D%2C%22center%22%3A%5B-6.013829868904978%2C36.043946519494064%5D%2C%22zoom%22%3A6%7D%7D
# https://www.kaggle.com/danielmartinalarcon/tanzanian-water-pumps/comments


# Data Description
# https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/page/25/


import pandas as pd 
import numpy as np 
import json

df=pd.read_csv("Table(0-20).csv")
print(df.head())  
print(len(df))    # 59400


# Column 1 - id
# Its an Assessment Variable and has Unique values
print(len(df["id"].unique()))  # 59400


# Column 2 - status_group
# Its the Classification Variable (functional,non functional, needs repair)
df_func=df[df["status_group"]=="functional"]
df_nonfunc=df[df["status_group"]=="non functional"]
df_repair=df[df["status_group"]=="functional needs repair"]
print(len(df_func))      # 32259  (54%)
print(len(df_nonfunc))   # 22824  (39%)
print(len(df_repair))    # 4317   (7%)


# Column 3 - amount_tsh
# Numerical Variable but has a lot of redundant values
print(len(df["amount_tsh"].unique()))    # 98
print(df["amount_tsh"].mean())           # 318
print(df["amount_tsh"].max())            # 3,50,000
print(df["amount_tsh"].min())            # 0
#print("hi")
print(len(df[(df["amount_tsh"]>318)&(df["status_group"]=="functional")]))   # 5k
print(len(df[(df["amount_tsh"]<318)&(df["status_group"]=="functional")]))   # 27k
print(len(df[(df["amount_tsh"]>318)&(df["status_group"]=="non functional")]))   # 1.5k
print(len(df[(df["amount_tsh"]<318)&(df["status_group"]=="non functional")]))   # 21k
print(len(df[(df["amount_tsh"]>318)&(df["status_group"]=="functional needs repair")]))   # 600
print(len(df[(df["amount_tsh"]<318)&(df["status_group"]=="functional needs repair")]))   # 3.7k
ans_dict={}
for i in df["amount_tsh"]:
	if i in ans_dict.keys():
		ans_dict[i]+=1
	else:
		ans_dict[i]=1
#print(ans_dict)          # For all unique values of amount_tsh, the number of times it occurs
#print(ans_dict.values())
f=open("amount_tsh.csv","w")
header=("amount_tsh,Count")
f.write(header+"\n")
for elem in ans_dict.keys():
	cs="{},{}".format(elem,ans_dict[elem])
	f.write(cs+"\n")
f.close()



# Column 4 - date_recorded
# Administrative variable 
# Oldest - 2002
# Newest - 2013


# Column 5,7 - Funder and Installer
# Since Funder has lesser values we can choose that over Installer
df_fund=df["funder"].unique()
print(len(df_fund))       # 1898
df_installer=df["installer"].unique()
print(len(df_installer))  # 2146
ct=0 
for i in df_fund:
	if i in df_installer:
		ct+=1
print(ct)                 # 488 common values
ans_dict={}
for i in df["installer"]:
	if i in ans_dict.keys():
		ans_dict[i]+=1
	else:
		ans_dict[i]=1
#print(ans_dict)          # For all unique values of Installer, the number of times it occurs
#print(ans_dict.values())
# dict_values([94, 39, 408, 222, 135, 17402, 192, 48, 143, 1050, 180, 397, 72, 111, 135, 2, 392, 71, 301, 3655, 17, 622, 75, 1060, 30, 270, 408, 107, 166, 1825, 14, 898, 1206, 55, 249, 147, 539, 278, 553, 25, 214, 125, 1, 30, 84, 80, 1, 84, 32, 610, 13, 16, 60, 5, 5, 840, 81, 31, 15, 2, 396, 121, 777, 3, 86, 133, 6, 96, 7, 199, 222, 14, 158, 119, 552, 92, 5, 114, 37, 1, 1, 14, 287, 707, 75, 103, 113, 28, 4, 329, 119, 173, 110, 40, 222, 125, 42, 52, 138, 95, 316, 152, 25, 208, 59, 234, 46, 551, 1, 149, 5, 1, 2, 80, 45, 27, 208, 7, 1, 55, 14, 17, 13, 60, 28, 19, 7, 154, 38, 1, 33, 103, 54, 1, 126, 5, 149, 23, 23, 27, 8, 65, 54, 47, 13, 175, 9, 25, 21, 123, 66, 24, 75, 55, 87, 1, 64, 383, 121, 7, 102, 97, 8, 34, 116, 11, 55, 6, 7, 3, 17, 156, 7, 27, 7, 162, 24, 246, 7, 2, 89, 22, 46, 8, 71, 13, 25, 5, 105, 142, 19, 25, 5, 3, 128, 21, 157, 23, 98, 9, 9, 100, 1, 141, 10, 1, 1, 65, 1, 20, 45, 7, 174, 8, 181, 6, 1, 3, 1, 12, 17, 55, 8, 202, 52, 7, 2, 8, 35, 6, 13, 13, 2, 22, 6, 3, 27, 9, 8, 60, 5, 100, 54, 3, 4, 97, 12, 1, 31, 19, 210, 22, 52, 5, 77, 12, 22, 78, 13, 22, 6, 69, 4, 15, 10, 42, 55, 2, 9, 47, 64, 91, 11, 25, 1, 2, 63, 16, 38, 22, 53, 34, 98, 1, 18, 9, 17, 26, 8, 6, 41, 27, 17, 29, 10, 9, 12, 13, 1, 47, 1, 7, 44, 2, 5, 3, 25, 224, 1, 1, 14, 1, 46, 31, 14, 26, 24, 6, 57, 1, 3, 14, 29, 19, 17, 3, 17, 17, 31, 8, 2, 1, 5, 69, 5, 12, 11, 37, 62, 24, 19, 89, 13, 50, 30, 32, 22, 84, 3, 6, 6, 15, 58, 1, 10, 13, 7, 36, 5, 5, 32, 2, 54, 5, 26, 4, 29, 4, 13, 42, 2, 29, 46, 1, 5, 9, 86, 15, 4, 2, 13, 4, 3, 9, 23, 6, 3, 5, 18, 6, 5, 4, 36, 11, 62, 28, 24, 16, 5, 8, 4, 4, 1, 4, 1, 2, 5, 5, 3, 32, 1, 12, 8, 1, 19, 31, 1, 24, 2, 9, 6, 12, 1, 2, 12, 3, 8, 20, 15, 8, 29, 4, 1, 12, 5, 1, 2, 7, 35, 8, 7, 24, 9, 6, 3, 1, 17, 1, 19, 1, 4, 24, 9, 5, 6, 20, 9, 14, 1, 45, 1, 33, 9, 10, 15, 1, 14, 2, 1, 12, 1, 7, 29, 10, 20, 13, 6, 1, 2, 4, 7, 9, 3, 12, 6, 33, 2, 7, 5, 10, 5, 31, 9, 18, 4, 2, 8, 1, 17, 7, 3, 1, 5, 7, 5, 15, 5, 30, 1, 4, 2, 1, 24, 1, 12, 7, 1, 23, 2, 18, 14, 1, 24, 21, 2, 13, 1, 1, 2, 1, 30, 8, 11, 27, 1, 9, 11, 21, 2, 13, 46, 5, 9, 3, 1, 1, 1, 23, 4, 2, 2, 3, 1, 2, 25, 10, 4, 15, 1, 15, 13, 29, 1, 22, 2, 2, 21, 3, 14, 3, 5, 3, 1, 23, 8, 1, 1, 52, 2, 10, 1, 11, 7, 1, 4, 6, 3, 10, 3, 1, 2, 33, 7, 14, 15, 13, 1, 22, 23, 7, 4, 2, 3, 2, 4, 7, 21, 41, 3, 5, 1, 21, 1, 1, 2, 17, 20, 1, 3, 3, 19, 5, 1, 1, 1, 23, 1, 12, 4, 23, 15, 3, 7, 10, 5, 2, 10, 6, 3, 15, 5, 1, 1, 1, 14, 3, 2, 1, 5, 2, 11, 5, 17, 2, 1, 11, 2, 1, 1, 18, 8, 5, 11, 2, 1, 10, 4, 2, 1, 1, 12, 3, 10, 1, 8, 7, 3, 1, 12, 1, 3, 1, 1, 1, 3, 1, 4, 10, 16, 9, 6, 1, 1, 5, 15, 24, 30, 1, 1, 1, 1, 4, 1, 2, 6, 2, 1, 1, 8, 5, 3, 9, 1, 6, 6, 3, 13, 4, 1, 1, 3, 3, 5, 4, 1, 1, 1, 5, 1, 15, 13, 1, 1, 1, 4, 1, 1, 3, 5, 3, 1, 1, 1, 2, 4, 7, 6, 1, 2, 4, 12, 23, 11, 1, 6, 1, 1, 33, 10, 6, 1, 2, 2, 17, 27, 3, 2, 1, 10, 5, 1, 2, 3, 1, 1, 1, 2, 21, 3, 20, 9, 1, 13, 2, 1, 5, 4, 1, 2, 1, 4, 2, 1, 1, 15, 1, 1, 2, 1, 1, 14, 1, 2, 1, 9, 8, 10, 7, 1, 1, 3, 1, 1, 7, 1, 1, 3, 5, 2, 1, 13, 5, 1, 2, 5, 2, 6, 2, 6, 1, 1, 10, 1, 6, 3, 1, 3, 15, 1, 1, 1, 10, 3, 10, 1, 1, 1, 13, 1, 2, 1, 9, 2, 2, 1, 19, 4, 7, 3, 1, 2, 2, 13, 12, 4, 1, 2, 3, 1, 4, 2, 13, 4, 2, 4, 1, 5, 9, 2, 4, 9, 1, 1, 3, 1, 1, 1, 1, 2, 2, 2, 4, 4, 3, 5, 1, 4, 1, 10, 1, 2, 1, 1, 6, 18, 1, 7, 4, 3, 3, 3, 1, 10, 7, 2, 2, 3, 1, 3, 1, 10, 12, 4, 4, 13, 1, 5, 3, 1, 1, 1, 2, 2, 6, 4, 2, 1, 1, 7, 1, 2, 3, 2, 2, 13, 3, 2, 6, 1, 1, 3, 4, 2, 1, 3, 5, 3, 1, 25, 1, 6, 2, 1, 1, 6, 8, 1, 2, 1, 2, 1, 9, 2, 2, 1, 1, 6, 1, 1, 1, 2, 1, 2, 5, 3, 12, 1, 2, 4, 4, 10, 1, 3, 1, 2, 1, 3, 2, 1, 1, 1, 5, 7, 2, 2, 4, 1, 1, 10, 1, 1, 1, 3, 1, 3, 1, 1, 3, 3, 2, 1, 4, 5, 1, 1, 7, 1, 1, 5, 2, 1, 2, 3, 1, 1, 15, 1, 2, 10, 6, 5, 1, 1, 1, 1, 2, 5, 1, 1, 2, 1, 1, 1, 10, 1, 4, 3, 1, 1, 5, 3, 1, 1, 4, 1, 1, 1, 1, 1, 2, 4, 3, 2, 4, 1, 1, 3, 6, 1, 10, 1, 1, 4, 1, 1, 1, 3, 2, 3, 1, 4, 4, 3, 2, 1, 1, 1, 1, 1, 3, 2, 5, 1, 5, 1, 1, 1, 2, 1, 3, 1, 2, 2, 4, 9, 1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 3, 3, 5, 1, 1, 1, 1, 16, 5, 3, 1, 1, 3, 1, 1, 1, 1, 2, 1, 19, 1, 4, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 4, 3, 2, 3, 2, 1, 3, 1, 1, 2, 3, 2, 1, 1, 2, 10, 17, 1, 1, 2, 1, 3, 13, 1, 1, 9, 1, 2, 1, 1, 1, 6, 1, 1, 5, 1, 3, 1, 4, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 2, 1, 1, 3, 3, 1, 1, 2, 1, 1, 4, 1, 1, 1, 3, 4, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 3, 2, 1, 1, 1, 1, 2, 4, 3, 1, 1, 3, 2, 2, 2, 1, 1, 2, 7, 2, 1, 5, 3, 1, 1, 1, 2, 4, 2, 1, 1, 2, 1, 2, 4, 4, 1, 1, 1, 1, 4, 1, 3, 1, 2, 2, 4, 2, 1, 1, 1, 3, 2, 1, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 6, 5, 2, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 2, 1, 1, 1, 3, 1, 1, 2, 1, 1, 4, 1, 1, 1, 2, 1, 7, 1, 3, 1, 2, 1, 1, 1, 1, 1, 9, 1, 3, 1, 1, 1, 1, 1, 1, 4, 2, 2, 1, 2, 8, 4, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 2, 3, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 5, 1, 2, 3, 1, 2, 1, 1, 1, 2, 1, 3, 1, 3, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 4, 1, 2, 1, 1, 2, 1, 3, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 5, 1, 3, 1, 1, 1, 3, 1, 1, 1, 2, 1, 3, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1, 3, 1, 2, 3, 2, 1, 1, 2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 3, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 3, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 5, 1, 2, 1, 3, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
f=open("Installer.csv","w")
header=("Installer,Count")
f.write(header+"\n")
for elem in ans_dict.keys():
	cs="{},{}".format(elem,ans_dict[elem])
	f.write(cs+"\n")
f.close()


# Column 6 - gps_height
print(len(df["gps_height"].unique()))    # 2428 Unique values
print(df["gps_height"].mean())           # Mean - 669
print(df["gps_height"].max()) 			 # Max - 2770
print(df["gps_height"].min()) 			 # Min - -90
mn_val=df["gps_height"].mean()
print(len(df[(df["gps_height"]>mn_val)&(df["status_group"]=="functional")]))   # 15k
print(len(df[(df["gps_height"]<mn_val)&(df["status_group"]=="functional")]))   # 16k
print(len(df[(df["gps_height"]>mn_val)&(df["status_group"]=="non functional")]))   # 8k
print(len(df[(df["gps_height"]<mn_val)&(df["status_group"]=="non functional")]))   # 14k
print(len(df[(df["gps_height"]>mn_val)&(df["status_group"]=="functional needs repair")]))   # 2k
print(len(df[(df["gps_height"]<mn_val)&(df["status_group"]=="functional needs repair")]))   # 2k


# Geographical locations - Columns 8,9 Latitude,Longitude 
# Latitude = 0-40.34
# Longitude = -11.6 to -2
print(len(df["latitude"].unique()))  # 58k
print(len(df["longitude"].unique())) # 58k


# Column 10 - wpt_name
# Too many unique values for it to have categories , cant be used as a numeric as well
# Has a lot of useless values as well
print(len(df["wpt_name"].unique()))   # 37k


# Column 11 - num_private
print(len(df["num_private"].unique()))  # 65
ans_dict={}
for i in df["num_private"]:
	if i in ans_dict.keys():
		ans_dict[i]+=1
	else:
		ans_dict[i]=1
#print(ans_dict)          # For all unique values of num_private, the number of times it occurs
#print(ans_dict.values())
f=open("num_private.csv","w")
header=("num_private,Count")
f.write(header+"\n")
for elem in ans_dict.keys():
	cs="{},{}".format(elem,ans_dict[elem])
	f.write(cs+"\n")
f.close()



# Out of all the geographical locations (Column 12-18), we can just keep Region
# Basin and subvillage are not suitable since they have a lot of useless and missing values
print(len(df["region"].unique()))  # 21
ans_dict={}
for i in df["region"]:
	if i in ans_dict.keys():
		ans_dict[i]+=1
	else:
		ans_dict[i]=1
#print(ans_dict)          # For all unique values of region, the number of times it occurs
#print(ans_dict.values())
f=open("region.csv","w")
header=("region,Count")
f.write(header+"\n")
for elem in ans_dict.keys():
	cs="{},{}".format(elem,ans_dict[elem])
	f.write(cs+"\n")
f.close()


# Column 19 - Population
# Can't determine whether categorical or numerical
# Even if we take it as categorical, we have to combine values to make new categories
print(len(df["population"].unique()))   # 1049
print(len(df[df["population"]==0]))     # 21k entries with 0 population
print(df["population"].max())			# 30500
print(df["population"].mean())			# 180
print(df["population"].min())			# 0
ans_dict={}
for i in df["population"]:
	if i in ans_dict.keys():
		ans_dict[i]+=1
	else:
		ans_dict[i]=1
#print(ans_dict)          # For all unique values of population, the number of times it occurs
#print(ans_dict.values())
f=open("population.csv","w")
header=("population,Count")
f.write(header+"\n")
for elem in ans_dict.keys():
	cs="{},{}".format(elem,ans_dict[elem])
	f.write(cs+"\n")
f.close()


# Column 20 - Public Meeting

# There are 3k Missing values

print(len(df[df["public_meeting"]==True]))
# True = 51k
print(len(df[df["public_meeting"]==False]))
# False = 5k

# True = Functional( 56% ) , Non Functional( 37% ) , Functional needs repair( 7% )
# False = Functional( 43% ) , Non Functional( 48% ) , Functional needs repair( 9% ) 
print(len(df[(df["public_meeting"]==False)&(df["status_group"]=="functional")]))   # 2k
print(len(df[(df["public_meeting"]==True)&(df["status_group"]=="functional")]))   # 28k
print(len(df[(df["public_meeting"]==False)&(df["status_group"]=="non functional")]))   # 2k
print(len(df[(df["public_meeting"]==True)&(df["status_group"]=="non functional")]))   # 18k
print(len(df[(df["public_meeting"]==False)&(df["status_group"]=="functional needs repair")]))   # 400
print(len(df[(df["public_meeting"]==True)&(df["status_group"]=="functional needs repair")]))   # 3.8k
