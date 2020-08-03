import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read data
test_set_orignal = pd.read_csv("Original.csv")
test_result = pd.read_csv('Test.csv')

#make copy of orignal test data set
test_set = test_set_orignal.copy()

#drop redundant columns
drop_list = ['id',
             'date_recorded',
            'amount_tsh',
            'funder',
            'longitude',
            'latitude',
            'wpt_name',
            'num_private',
            'basin',
            'subvillage',
            'region_code',
            'district_code',
            'installer',
            'lga',
            'ward',
            'recorded_by',
            'scheme_name',
             'scheme_management',
            'extraction_type',
            'extraction_type_class',
            'management_group',
            'payment',
            'water_quality',
            'quantity',
            'source',
            'source_class',
            'waterpoint_type']
test_set.drop(columns = drop_list, inplace = True)
print(test_set.columns)
# Index(['status_group', 'gps_height','region', 'population',
#        'public_meeting', 'permit', 'construction_year',
#        'extraction_type_group', 'management', 'payment_type', 'quality_group',
#        'quantity_group', 'source_type', 'waterpoint_type_group'],
#       dtype='object')

#delete missing data
test_set.construction_year.replace(0, np.nan, inplace = True)
test_set.replace('unknown', np.nan, inplace = True)
test_set.replace('other', np.nan, inplace = True)
test_set.dropna(inplace = True)
print(test_set.index.size, '\n', test_set)
print(test_set.status_group.value_counts())