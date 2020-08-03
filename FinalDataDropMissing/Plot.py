import pandas as pd 
import numpy as np 
import csv

import matplotlib.pyplot as plt 

df1=pd.read_csv("final_data_popcat.csv")
df1=df1.rename(columns={"Unnamed: 0":"Id"})
# print(df1.head())

# ==================================================================
# print(df1.groupby(["region", 'status_group']).size())
# region         status_group           
# Arusha         functional                 1304
#                functional needs repair      80
#                non functional              314
# Dar es Salaam  functional                  134
#                functional needs repair       3
#                non functional              109
# Iringa         functional                 3817
#                functional needs repair     117
#                non functional              854
# Kigoma         functional                  721
#                functional needs repair     461
#                non functional              305
# Kilimanjaro    functional                 2242
#                functional needs repair     218
#                non functional              909
# Lindi          functional                  325
#                functional needs repair      69
#                non functional              301
# Manyara        functional                  888
#                functional needs repair      84
#                non functional              310
# Mara           functional                  203
#                functional needs repair       8
#                non functional              217
# Morogoro       functional                 1952
#                functional needs repair     290
#                non functional              945
# Mtwara         functional                  455
#                functional needs repair      94
#                non functional              468
# Mwanza         functional                   67
#                functional needs repair      14
#                non functional               29
# Pwani          functional                 1347
#                functional needs repair      18
#                non functional              762
# Rukwa          functional                  617
#                functional needs repair     109
#                non functional              505
# Ruvuma         functional                 1147
#                functional needs repair     115
#                non functional              541
# Shinyanga      functional                   56
#                functional needs repair      62
#                non functional                8
# Singida        functional                  548
#                functional needs repair      63
#                non functional              359
# Tanga          functional                 1252
#                functional needs repair      68
#                non functional              650


# print(df1.groupby(["region", 'status_group']).size().unstack())
# region                                                            
# Arusha               1304                       80             314
# Dar es Salaam         134                        3             109
# Iringa               3817                      117             854
# Kigoma                721                      461             305
# Kilimanjaro          2242                      218             909
# Lindi                 325                       69             301
# Manyara               888                       84             310
# Mara                  203                        8             217
# Morogoro             1952                      290             945
# Mtwara                455                       94             468
# Mwanza                 67                       14              29
# Pwani                1347                       18             762
# Rukwa                 617                      109             505
# Ruvuma               1147                      115             541
# Shinyanga              56                       62               8
# Singida               548                       63             359
# Tanga                1252                       68             650


# df1.groupby(["region", 'status_group']).size().unstack().plot(kind='bar',stacked=True)
# plt.show()
# df1.groupby(["region", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()

#===============================================================================

# print(df1.groupby(["installer", 'status_group']).size()) #Length: 1556
# df1.groupby(["installer", 'status_group']).size().unstack().plot(kind='bar',stacked=True)
# plt.show()
# df1.groupby(["installer", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()

#=================================================================================

# df1.groupby(["installer", 'status_group']).size().unstack().plot(kind='bar',stacked=True)
# plt.show()
# df1.groupby(["installer", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()
#===============================================================================

# df1.groupby(["installer", 'status_group']).size().unstack().plot(kind='bar',stacked=True)
# plt.show()
# df1.groupby(["installer", 'status_group']).size().unstack().plot(kind='bar',stacked=False)
# plt.show()

#=================================================================================


# Box Plots
# Numerical Variables (3) - 'gps_height','population','construction_age'  

#===========================================================================
# gps_height
# df1.boxplot(by="status_group",column=["gps_height"],grid=False)
# plt.show()

#===============================================================================