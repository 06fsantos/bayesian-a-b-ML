'''
Created on 23 Feb 2018

@author: filipe
'''
'''

Visualise the approximated Gaussian that results from the Central Limit Theorem
And then compare that to the Bayesian Beta Posterior

'''  
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta, norm

T = 501      ###### number of trials
true_ctr = 0.5
a, b = 1, 1  ####### set the beta priors to be non-informative --> uniform distribution
plot_indices = (10, 20, 30, 50, 100, 200, 500)   ######## tells us when to plot
data = np.empty(T)

for i in range(T):
    x = 1 if np.random.random() < true_ctr else 0
    data[i] = x
    
    a += x
    b += 1-x 
    
    if i in plot_indices:
        p = data[:i].mean()     ######## estimated click through rate 
        n = i + 1
        st_dev = np.sqrt(p*(1-p)/n)
        
        
        x = np.linspace(0,1,200)
        g = norm.pdf(x, loc=p, scale = st_dev)
        plt.plot(x, g, label = 'Gaussian Approximation')
        
        posterior = beta.pdf(x, a=a, b=b)
        plt.plot(x, posterior, label = 'Beta Posterior')
        
        plt.legend()
        plt.title('N: {}'.format(n))
        plt.show()


if __name__ == '__main__':
    pass