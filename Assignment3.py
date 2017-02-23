#!/usr/bin/env python3

#Anna E. Hiller
#Assignment 3, Feb. 22 2017

#1. Import
# Importing the binomial and uniform classes from the stats module of the scipy library
from scipy.stats import binom, uniform

# Importing pseudo-random number generators for uniform and Gaussian distributions
from random import random, gauss

#2. Define some data - Binomial
# Defining the data
flips = ["H","T","T","T","H"]
n = len(flips) 
k = sum([1 for fl in flips if fl == "H"])

#3. Define a function to calculate a likelihood, if p<0 or p>1
def like(k, n, p, testingPrior=False):
"""function to call a likelihood"""
    if testingPrior:  
        return 1      
    if p < 0:
        return 0
    elif p > 1:
        return 0
    else:
        return binom.pmf(k, n, p)
    
#4. Define a function to calculate a prior probability
# Defining function to calculate prior density - uniform [0,1]
def prior(p):
"""function to calculate a prior probability"""
    return uniform.pdf(p)

# Defining function to calculate the unnormalized posterior density
def post(k, n, p):
"""function to calculate the unnormalized posterior density"""
    posterior = prior(p) * like(k, n, p)
    return posterior

#5. Define a function to draw a new value for the parameter(s) of interest using
# a proposal distribution

#import numpy
import numpy as np
def draw(n, p, sim):
"""function to draw a new value of a parameter from a proposal distribution"""
    # n = number of trials, p = probability of each trial         
    # sim = number of simulations, output 
    value = [np.random.binomial(n, p, sim)] #proposal distribution is binomial
    # result of simulating (k successes), tested x times (sim)
    print (value)
	
#From: https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.binomial.html

#6. Define a function to accept or reject proposed moves based on the ratio of
# their posterior densities.

#propose a new value (i.e., draw it from your proposal distribution)
#calculate the posterior probability (or probability density) of your proposed state
#calculate the posterior probability (or probability density) of your current state
#take their ratio

def reject(k, n, p):
"""function to accept or reject proposed moves based on the ratio of their 
posterior densities"""
	#propose a new value, simulated 10 times as default
    diff = 0.1
    listMCMC = []
    for k in value: #draw value from proposal distribution                      
        #calc posterior probability 
        p_curr = post(k, n, p)
        p_proposed = post(k, n, (p_curr + diff)
        p_accept = p_proposed/p_current
    	if p_accept >= 1
    	print("accept")
    	listMCMC.append(p_proposed)
   		if p_accept <1
    		print("accept sometimes")
    		if np.random.rand() < p_accept:
    			print("accept")
    			listMCMC.append(p_proposed)
    		else:
    			print("reject")
    if accept:
    	p_curr = p_proposed
    	
#From: http://twiecki.github.io/blog/2015/11/10/mcmc-sampling/

#based on the rules defined for MCMC
#accept the proposal and add it to the chain
#or stay where you are


#7. Create lists to store parameter values, prior probabilities, likelihoods, 
# and posterior densities.
class values(object):
	def __int__ (self,n_trials,p_prob,k_success,prior_prob,like, post_den):
	
#OR

listMCMC = []
listMCMC.append(n, p, k, prior, like, post)
	

#8. Define a function to run the chain! Begin by defining starting conditions for
# the Markov chain, including the number of generations it will run, the 
# starting parameter value(s), and the starting posterior density 
# (unnormalized). Use a for loop to iterate through the specified number of 
# generations. Each step will involve proposing new values, deciding whether
# to accept or reject those values, then recording the new value. It can be very 
#cumbersome and unnecessary to record _every_ parameter value that's sampled.
#How could you write out values every n-th generation?

#define starting conditions for Markov Chain: number of generations run, starting
#parameter values, starting posterior density (arguments are # generations, lists to 
#store values, etc.)

def MCMC(n_trials, p_prob, generations, lists):
"""function to run a Markov Chain"""
	#use a for loop to iterate through the number of generations
	for i in 

#each step: (1) propose new value, (2) decide to accept or reject, 
#(3) and record new value
	reject (n, p)
	listMCMC = []
	listMCMC.append(values)
	
#I'm confused about how this is different from the accept/reject function above!? Also, 
#what do you mean by write out values every n-th generation!?!
	
#9. Create trace plots of parameter values, priors, likelihoods, and posteriors.
import numpy as np
import matplotlib.pyplot as plt

posterior = sampler() #from above
x = plt.subplot()
x.plot(posterior)

From: http://twiecki.github.io/blog/2015/11/10/mcmc-sampling/

#10. Create histograms of parameter values, priors, likelihoods, and posteriors.

x = plt.subplot()
sns.distplot function

#Since we never went over how to plot in class I have no idea how to make this work.
#I googled a few things and included the plot calls I think are needed.


"""
Now use the code you've written above to explore answers to these questions. 
Ideally, the code you've written is sufficiently generic, so you can simply
call the code above with different arguments. This will make it much easier to
remember the conditions you explored. If you write this assignment in a
Jupyter notebook, you can also include the answers as comments, plots, etc.
(1) How does the size of the proposal distribution affect the efficiency of
    the chain? Try a very small distribution, a very large one, and one that 
    seems like it should be about the width of the posterior peak.
    
(2) How long does it take for the chain to "burn in"? Try this with different
    proposal distributions and datasets of different sizes.
    
(3) Define a dataset where the values could be draws from a Normal. Have the
    chain explore the joint posterior distribution for both the mean and the
    standard deviation. Remember that you'll need to include proposals that 
    change both parameter values. What happens when the starting values for one
    or both parameters are very far away from the peak of the posterior? Try
    plotting the two parameter values from each generation against each other.
    Do they seem correlated?
    
(4) How confident are you that you've sampled the posterior distribution well?
    What strategies can you use to make sure? Can you run multiple, independent
    analyses using the code you wrote above?
"""

#I have no idea how to test these questions without a working MCMC sampler. Help!?




