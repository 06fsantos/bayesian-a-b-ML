'''
Created on 19 Feb 2018

@author: filipe
'''
import pandas as pd 
from scipy import stats

df = pd.read_csv('advertisement_clicks.csv')
a = df[df['advertisement_id'] == 'A']
b = df[df['advertisement_id'] == 'B']
a = a['action']
b = b['action']

print ('A mean: {}    B mean: {}'.format(a.mean(), b.mean()))

t, p = stats.ttest_ind(a,b)

print ('t value: {}       p-value: {}'.format(t , p))
