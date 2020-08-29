import numpy as np
import pandas as pd

male_names  = pd.read_csv('./indian-names/Indian-Male-Names.csv')
female_names = pd.read_csv('./indian-names/Indian-Female-Names.csv')

health_data = pd.read_csv('./500_Person_Gender_Height_Weight_Index.csv')

health_data['name'] = 'default'

male_count   = 0
female_count = 0

for index, row in health_data.iterrows() :
  if row['Gender'] == 'Male':
    health_data['name'][index] = male_names['name'][male_count]
    male_count +=1
  else:
    health_data['name'][index] = female_names['name'][female_count]
    female_count +=1

health_data.to_csv('patients.csv')