'''
Created on 23 Feb 2018

@author: filipe
'''
###### see how click through rate converges to the best bandit #######
import matplotlib.pyplot as plt
import numpy as np
from bayesian_bandit_in_code import Bandit

def run_experiment(p1, p2, p3, N):   ######## we are going to have 3 bandits, so 3 Ps
    bandits = [Bandit(p1), Bandit(p2), Bandit(p3)]
    
    data = np.empty(N)  ##### keeps track of all the data we have, 1=click, 0=no_click
    for i in range(N):
        j = np.argmax([b.sample() for b in bandits])
        x = bandits[j].pull()
        bandits[j].update(x)
        data[i] = x
        
    cumulative_average_ctr = np.cumsum(data) / (np.arange(N) + 1)  ######## divide by the N at that point
    
    plt.plot(cumulative_average_ctr)
    plt.plot(np.ones(N) * p1)
    plt.plot(np.ones(N) * p2)
    plt.plot(np.ones(N) * p3)
    plt.ylim((0,1))
    plt.xscale('log')
    plt.show()
    

if __name__ == '__main__':
    run_experiment(0.2,0.25,0.3, 100000)