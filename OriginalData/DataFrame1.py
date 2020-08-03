import pandas as pd 
import numpy as np 

df=pd.read_csv("Table(0-20).csv")
print(df.head())  
print(len(df))   # 59400

print(df.columns)   # Index(['id', 'status_group', 'amount_tsh', 'date_recorded', 'funder','gps_height', 
#'installer', 'longitude', 'latitude', 'wpt_name','num_private', 'basin', 'subvillage', 'region', 'region_code',
#'district_code', 'lga', 'ward', 'population', 'public_meeting'],dtype='object')

df1=df.copy()
df2=df.copy()

df1=df.where(df["amount_tsh"]>0)   # The rows that dont satisfy the condition have Nan 
print(len(df1))                    # 59400
df2=df[df["amount_tsh"]>0]         # Without using where function, removes Nan values as well
print(len(df2))         		   # 17761
print(df2.head())
print(df1.head())     # Gives a boolean mask


# df['country'] = df.index   # Changing index of the dataframe
# df = df.set_index('Gold')
# df.head()
# df = df.reset_index()
# df.head()

# df = df.set_index([df.index, 'Name'])
# df.index.names = ['Location', 'Name']
# df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))


print(df["amount_tsh"].count())    # 59400
print(df1["amount_tsh"].count())   # 17761

df1=df1.dropna()   # Drop rows with no values
print(len(df1))   # 16918

print(len(df[(df["gps_height"]>1800)&(df["status_group"]=="functional")]))   # 2219
print(len(df[(df["gps_height"]<1800)&(df["status_group"]=="functional")]))   # 30,029

print(df["num_private"].unique())   # All unique elements

geo_columns=['longitude', 'latitude', 'wpt_name','num_private', 'basin', 'subvillage', 'region', 'region_code',
'district_code', 'lga', 'ward']
df3=df[geo_columns]   # Keep only geographical data
print(df3.head())

df4=df3.set_index(["lga","ward"])   # Combines two columns
print(df4.head())
print(df4.loc["Ludewa","Mundindi"]) # loc is used to set index hierarchy after using set_index method

df5=df.set_index("id")
df5=df5.sort_index()   # Sorts based on the current Index
print(df5.head())
#       status_group  amount_tsh  ... population public_meeting
# id                              ...                          
# 0   non functional         0.0  ...          0            NaN
# 1       functional         0.0  ...         20           True
# 2       functional         0.0  ...          0           True
# 3       functional        10.0  ...         25           True
# 4   non functional         0.0  ...          0           True

# Mean and other statistical info that is calculated using numpy essentially ignores Nan and None

