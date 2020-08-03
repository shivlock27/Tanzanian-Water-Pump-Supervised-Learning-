import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

#read data
train_set_orignal = pd.read_csv('train_set.csv')
train_result_orignal = pd.read_csv('train_result.csv')

#make copy of original data set
train_set = train_set_orignal.copy()
train_result = train_result_orignal.copy()

#drop redundant columns
drop_list = ['id',
             'date_recorded',
             'installer',
             'amount_tsh',
             'funder',
             'longitude',
             'latitude',
             'wpt_name',
             'num_private',
             'basin',
             'management',
             'public_meeting',
             'subvillage',
             'region_code',
             'district_code',
             'lga',
             'ward',
             'recorded_by',
             'scheme_management',
             'scheme_name',
             'extraction_type',
             'extraction_type_class',
             'extraction_type_group',
             'management_group',
             'payment',
             'water_quality',
             'quantity',
             'source',
             'source_class',
             'waterpoint_type']

train_set.drop(columns = drop_list, inplace = True)
train_result.drop(columns = ['id'], inplace = True)

#delete missing/useless training data
train_set = train_set.join(train_result)

train_set.replace('other', np.nan, inplace = True)
train_set.replace('unknown', np.nan, inplace = True)

train_set.construction_year.replace(0, np.nan, inplace = True)

train_set = train_set[train_set.population < 10000]

train_set.waterpoint_type_group.replace(['cattle trough', 'dam', 'improved spring'], np.nan, inplace = True)

train_set.source_type.replace(['dam', 'rainwater harvesting'], np.nan, inplace = True)

quality_group_other_list = ['salty', 'good']
train_set.quality_group = train_set.quality_group.apply(lambda x : x if x in quality_group_other_list else 'other')

train_set.dropna(inplace = True)

train_result = pd.DataFrame(train_set.status_group.copy())
train_set.drop(columns = ['status_group'], inplace = True)

#convert numerical data to float
numerical_data = ['gps_height',
                  'population',
                  'construction_year']
train_set[numerical_data] = train_set[numerical_data].astype('float64')

#transform construction year to age
max_construction_year = train_set.construction_year.max()
train_set['construction_age'] = train_set.construction_year.apply(lambda x: max_construction_year - x)
train_set.drop(columns = ['construction_year'], inplace = True)

#convert string data to category and encode it
categorical_data = ['region',
                    'permit',
                    'payment_type',
                    'quality_group',
                    'quantity_group',
                    'source_type',
                    'waterpoint_type_group']

train_set[categorical_data] = train_set[categorical_data].astype('category')
train_result = train_result.astype('category')

train_set = pd.get_dummies(train_set)
train_set.reset_index(drop = True, inplace = True)
train_result['is_functional'] = train_result['status_group'].apply(lambda x : 1 if x == 'functional' else 0)
train_result.drop(columns = ['status_group'], inplace = True)
train_result.reset_index(drop = True, inplace = True)

X_train, X_test, Y_train, Y_test = train_test_split(train_set, train_result['is_functional'], test_size = 0.3)

lr = LogisticRegression(max_iter = 2000)
lr.fit(X_train, Y_train)
print(lr.score(X_test, Y_test))
print(confusion_matrix(Y_test, lr.predict(X_test)))

rf = RandomForestClassifier()
rf.fit(X_train, Y_train)
print(rf.score(X_test, Y_test))
print(confusion_matrix(Y_test, rf.predict(X_test)))