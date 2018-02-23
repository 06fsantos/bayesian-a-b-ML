'''
Created on 23 Feb 2018

@author: filipe
'''
import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import beta

NUM_TRIALS = 2000
BANDIT_PROBABILITIES = [0.2, 0.5, 0.75]  ### True click through rates

class Bandit():
    def __init__(self, p):   #### essentially going to act like a slot machine
        self.p = p   #### probability of winning 
        self.a = 1   #### beta parameters --> proirs will be 1 - gives a uniform distribution 
        self.b = 2
        
    def pull(self):
        return np.random.random() < self.p ##### if < p we get 1, if not we get 0 (either True or False)
    
    def sample(self):
        return np.random.beta(self.a, self.b)
    
    def update(self, x):   ####### using formula derived when looking at conjugate priors 
        self.a += x
        self.b += (1-x)

def plot(bandits, trial):  ###### plot the PDF of each bandit so we can compare them on the same chart 
    x = np.linspace(0,1,200)
    for b in bandits:
        y = beta.pdf(x, b.a, b.b)
        plt.plot(x, y, label = 'real p: {}'.format(b.p))
    plt.title('Bandit distributions after {} trials'.format(trial))
    plt.legend()
    plt.show()
       
def experiment(): 
    bandits = [Bandit(p) for p in BANDIT_PROBABILITIES]
    
    
    sample_points = [5, 10, 20 ,50, 100, 200, 500, 1000, 1500, 1999]
    for i in range(NUM_TRIALS):
        bestb = None
        max_sample = -1
        all_samples = []
        for b in bandits:
            sample = b.sample()
            all_samples.append(sample)
            if sample > max_sample:
                max_sample = sample 
                bestb = b
        if i in sample_points:
            print ('Current Samples: {}'.format(all_samples))
            plot(bandits, i)
            
        x = bestb.pull()
        bestb.update(x)
                   
    
if __name__ == '__main__':
    experiment()
    
    
    
    
    
    
    
    
    