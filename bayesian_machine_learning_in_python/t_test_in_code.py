'''
Created on 19 Feb 2018

@author: filipe
'''
import numpy as np
from scipy import stats 



if __name__ == '__main__':
    N = 10
    a = np.random.randn(N) + 2
    b = np.random.randn(N)
    
    var_a = a.var(ddof = 1)
    var_b = b.var(ddof = 1)
    
    s = np.sqrt((var_a + var_b) / 2)
    t = (a.mean() - b.mean()) / (s*np.sqrt(2.0/N))
    
    df = 2 * N - 2
    p = 1 - stats.t.cdf(t, df = df)
    
    print ('t: {}  p: {}'.format(t, 2*p))
    
    t2, p2 = stats.ttest_ind(a,b)
    print ('t: {}  p: {}'.format(t2, p2))