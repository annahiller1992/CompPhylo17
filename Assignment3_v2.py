#!/usr/bin/env python3

#Anna E. Hiller
#Assignment 3, Feb. 22 2017

#1. Import
# Binomial and uniform classes from the stats module of the scipy library
from scipy.stats import binom, uniform, norm
# Pseudo-random number generators for uniform and Gaussian distributions
from random import random, gauss
# Plot tools
import matplotlib.pyplot as plt
import numpy as np

#2. Define a function to calculate a likelihood, if p<0 or p>1
def like(n, k, p, testingPrior=False):
    """function to call a likelihood"""
    if testingPrior:
        return 1
    if p < 0:
        return 0
    elif p > 1:
        return 0
    else:
        return binom.pmf(n, k, p)
    
#3. Define a function to calculate a prior probability
# Defining function to calculate prior density - uniform [0,1]
def prior(p):
    """function to calculate a prior probability"""
    return uniform.pdf(p)
    
#Normal Version
#def prior(p):
#    return norm.pdf(p)

#4.  Defining function to calculate the unnormalized posterior density
def post(n, k, p):
    """function to calculate the unnormalized posterior density"""
    posterior = prior(p) * like(n, k, p)
    return posterior

#5. Define a function to draw a new value for the parameter(s) of interest using
# a proposal distribution
def drawNew():
    """function to draw a new value of a parameter from a proposal distribution"""
    new = np.random.normal(0, 0.1, 1)
    #new = norm.rvs(size=1) #for drawing from a normal distribution, not bounded 0-1
    return new
    

#6. Define a function to accept or reject proposed moves based on the ratio of
# their posterior densities.

#propose a new value (i.e., draw it from your proposal distribution)
#calculate the posterior probability (or probability density) of your proposed state
#calculate the posterior probability (or probability density) of your current state
#take their ratio

def acceptReject(n, k):
    """function to accept or reject proposed moves based on the ratio of their
    posterior densities"""
    #calc posterior probability 
    p = 0.1
    iter = []
    p_new = drawNew
    den_curr = post(n, k, p)
    den_proposed = post(n, k, p_new)
    ratio = den_proposed/den_curr
    if ratio >= 1:
        print("accept")
        iter.append(p_new)
    if p_accept <1:
        print("accept sometimes")
    if np.random.rand() < p_accept:
        print("accept")
        iter.append(p_new)
    else:
        print("reject")
        iter.append(p)
    if accept:
        p = p_new
            

#From: http://twiecki.github.io/blog/2015/11/10/mcmc-sampling/

""" class notes """

""".rvs -> means give me random draws
arguments -> (loc = p_curr)

p = 0.1
iter = []
iter.append(p)
for _ in ngen:
    p_new = drawNew(p)
    r = calcRatio (p_new, p)
    p = choose(r, p_new, p)
    iter.append(p)
    uniform.rbs

from scipy import stats
help(stats)
help(stats.norm)"""


"""Create lists to store parameter values, prior probabilities, likelihoods, 
# and posterior densities.
class values(object):
    def __int__ (self,n_trials,p_prob,k_success,prior_prob,like, post_den):
    
#OR
listMCMC = []
listMCMC.append(n, p, k, prior, like, post)"""


#7. Define a function to run the chain! Begin by defining starting conditions for
# the Markov chain, including the number of generations it will run, the 
# starting parameter value(s), and the starting posterior density 
# (unnormalized). Use a for loop to iterate through the specified number of 
# generations. Each step will involve proposing new values, deciding whether
# to accept or reject those values, then recording the new value. It can be very 
#cumbersome and unnecessary to record _every_ parameter value that's sampled.
#How could you write out values every n-th generation?

#because samples are autocorrelated, want to space out (to summarize). Use % function
#(from .......). Use if statement, if generation is multiple of 10 -> store as list, 
#print to screen, store as file

#define starting conditions for Markov Chain: number of generations run, starting
#parameter values, starting posterior density (arguments are # generations, lists to 
#store values, etc.)

def chain(n, k, n_gen):
    """function to run a Markov Chain"""
    #use a for loop to iterate through the number of generations
    parameters_data = []
    prior_data = []
    likelihood_data = []
    posteriors_data = []
    for i in range(0,n_gen):
        acceptReject(n, k)
        parameters_data.append(n, k)
        prior_data.append(prior(p))
        likelihood_data.append(like(n, k, p))
        posteriors_data.append(post(k, n, p))
#PROBLEM: for some reason I am getting an error at the prior calculation. When I went 
#back and checked the values, the function prior always returns 0. Huh!? I feel like I'm
#on the right track here but am getting stuck on the structure.

"""class notes"""
"""#each step: (1) propose new value, (2) decide to accept or reject, 
#(3) and record new value
    reject (n, p)
    listMCMC = []
    listMCMC.append(values)"""
    
#9. Create trace plots of parameter values, priors, likelihoods, and posteriors.
fig,ax=plt.subplots()
ax.plot(prior_data) #change data input here, for each of the lists generated by chain()
x=ax.set(xlabel='Samples',ylabel='Priors') #change labels here
plt.show()

#10. Create histograms of parameter values, priors, likelihoods, and posteriors.
numBins = 50
plt.hist(prior_data) #change input data
plt.title("Priors") #change title here
plt.xlabel("Priors") #change xlabel here
plt.ylabel("Generations") #change ylabel here
plt.show()

#From: week 2 intro to likelihood, likelihood ratio test
#But since I couldn't get my sampler to work I'm not sure how to actually get 
#anything to plot... Could also use plt.(plot)


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

#I have no idea how to test these questions without a working MCMC sampler. Help!? I'm
#really trying my best here but still am very confused... I get the simple examples
#in class (e.g. coin flipping analogy) but the more complicated implementations
#and how to actually make them run is not going well...


