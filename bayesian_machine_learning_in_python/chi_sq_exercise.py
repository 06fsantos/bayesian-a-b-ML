'''
Created on 20 Feb 2018

@author: filipe
'''
import pandas as pd 
import numpy as np 
from scipy.stats import chi2

def retrieving_information(data):
    a = data[data['advertisement_id'] == 'A']
    b = data[data['advertisement_id'] == 'B']
    a = a['action']
    b = b['action']
    
    A_clk = a.sum()
    A_noclk = a.size - a.sum()
    B_clk = b.sum()
    B_noclk = b.size - b.sum()
    T = np.array([[A_clk, A_noclk], [B_clk, B_noclk]])
    return T

def get_p_value(T):
    ########### same as scipy.stats.chi2_contingency(T, correction=False)
    det = T[0,0] * T[1,1] - T[0,1] * T[1,0]
    c2 = float(det) / T[0].sum() * det / T[1].sum() * T.sum() / T[:,0].sum() / T[:,1].sum()
    p = 1 - chi2.cdf(c2, df = 1)
    return p
    


if __name__ == '__main__':
    df = pd.read_csv('advertisement_clicks.csv')
    print (get_p_value(retrieving_information(df)))