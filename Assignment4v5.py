#!/usr/bin/env python3

#Anna E. Hiller
#Assignment 4, Week of March 04 2017
#Second Version poster with notes from class as well

"""
Part 1: Define a Markov chain class
	- Start with a discrete-state, discrete-time chain
	- Be able to run multiple replicates
	- Be able to summarize frequencies of states across replicates for particular iterations
	- Be able to calculate the probability of a set of states
		- Going forward
		- Going backward
"""

#Part1
"""
We will need to draw random numbers (using random) and we will need to use
some special functions for matrices (using numpy).
"""
import random
import numpy as np

class MarkovChain(object):
    """
    A discrete-state, discrete-time Markov chain.
    """
    def __init__(self, stateSpace, tMatrix=np.matrix([[0.7, 0.3], [0.3, 0.7]]), iter=10, nchains=1, simChain, simStates, start, end):
    #Initializing variables that are necessary for simulating a discrete-time Markov chain
        self.stateSpace = [] # state space
        self.tMatrix = tMatrix # Q-matrix
        self.iter = iter # number of iterations
        self.nchains = chains # number of chains
        self.simChain = [] #list of simulated chains
        self.simStates = [] # list of lists to hold simulated chains
        self.start = start
        self.end = end
                    
    def discSamp(self,states=[],probs=[]):
        """
        Samples from an arbitrary discrete distribution.
        States and probs lists must be equal in length. Probs must sum to 1.
        """
        r = random.random()
        cumulProb = 0
        index = 0
        for p in probs:
            cumulProb = cumulProb + p
            if r < cumulProb:
                return states[index]
            index += 1
        print("ERROR: Probabilities did not add to 1!")

    def run(self,startState=0):
        """
        Method to simulate the states sampled by a Markov chain.
        """
        # Reset chains here to empty list of lists
        self.simChain = []
        self.simStates = []
        for for chain in range(0,nchains):
            # Initialize this chain to an empty list
            self.simState.append(chain)
            # Add starting state to this chain
            self.simChain.append(start)
            # For loop across iterations for this chain
            for iter in range(0,iter):
                state = self.discSamp(self.states, self.tMatrix[stateSpace.index(state)])
                # Add the new state to this chain.
                self.simChain.append(state)
        
    def showChain(self, chain = 1):
        print ("for printing entire chain chain = 0, for iterations chain = 1")
        """
        Method to simply print out the states sampled by a chain. Provide
        ability to print a particular iteration of a chain or the whole chain.
        """
        if chain = 1:
            # Print out entire chain
            print(self.simChain)
        else chain = 0:
            # Print just that iteration in that chain
            print(self.simChain.append(state))
        elif:
            print ("error showing chains, chain = 1 or 0")
            
    def stateFreqs(self,state=[simStates.index(state)],start=[0,0],end=[iter, iter]):
        """
        Method to calculate and print the frequencies of a particular state
        across chains.
        """
        if end is None:
            # By default, set end to last iteration
            end = self.iter
        # Initialize list of frequencies
        freqs = []
        # For loop from start iteration to end iteration
        for iter in range(0,iter):
            # Initialize variable to hold counts of state across chains
            count = 0
            # For loop across chains
            for chain in range(0,nchains):
                # Check if the current state is the state of interest
                if curr == state:
                    # If so, add to the count
                    count += 1
            # Divide by total num of chains and add freq to list
            freq = count/nchains
            freqs.append(freq)
        # Print or return the list of frequencies
            print freqs

    def forwardProb(self, chain = [self.nchains.index(chain)]):
        """
        Calculate the probability of observing the full set of states 
        simulated for a particular chain, assuming the chain went in a 
        forward direction.
        """
        # Initialize the probability to 1.0
        prob = 1
        # For loop across iterations     
        for chain in range(0,nchains):
            # Find the index of the state for the current iteration (A)
            curr = [self.simStates.index(state)]
            # Find the index of the state for the next iteration (B)
            next = [self.simStates.index(state + 1)] #plus 1 for forward
            # Multiply overall probability by P(B|A) using Q-matrix
            prob *= numpy.matrix(self.tMatrix)
        # Return the probability
        return prob
    
    def reverseProb(self, chain = [self.nchains.index(chain)]):
        """
        Calculate the probability of observing the full set of states 
        simulated for a particular chain, assuming the chain went in a 
        REVERSE direction.
        
        The code for this method is just like forwardProb, but your for
        loop should run in reverse - from the end of the chain back to the
        beginning.
        """
         # Initialize the probability to 1.0
        prob = 1
        # For loop across iterations     
        for chain in range(0,nchains):
            # Find the index of the state for the current iteration (A)
            curr = [self.simStates.index(state)]
            # Find the index of the state for the next iteration (B)
            next = [self.simStates.index(state - 1)] #minus 1 for reverse
            # Multiply overall probability by P(B|A) using Q-matrix
            prob *= numpy.matrix(self.tMatrix)
        # Return the probability
        return prob
       
    def margForwardProb(self, chain = [self.nchains.index(chain)], E = end):
        """
        Calculate the MARGINAL probability of starting in one state and ending
        in another, considering all possible intermediates.
        """
        # Raise your Q-matrix to the power of the number of iterations
        numpy.linalg.matrix_power(numpy.matrix(self.tMatrix),self.iter)
        # Find the index of the starting state for the chain (S)
        start = [self.simStates.index(state)]
        # Find the index of the ending state for the chain (E)
        end = [self.simStates.index(state + E)]
        # Look up P(E|S) in the new matrix
        prob *= numpy.matrix(self.tMatrix)
        # Return the relevant probability       
        return prob
        
"""
Part 2: Extend (or define a new) class for discrete-state, continuous-time chains
	- Be able to simulate waiting times and draws of new states
	- If you know stationary frequencies, be able to normalize Q-matrix
		- i.e., weighted average of diagonal entries is 1
	- Be able to calculate the probability of a sequence of changes
		- Going forward
		- Going backward
		

Variables:
    - state space
    - Q matrix (transition matrix)
    - branch length
    - number of sites
    - list of simulated states (or list of lists for >1 site)
    - list of waiting times (or list of lists for >1 site)
    - starting sequence (empty if simulating)
    - ending sequence (empty if simulating)
"""
#Part2 - continuous

#####################################################
#                     In Class Notes                #
#####################################################

class MarkovChain(object):
    """
    A discrete-state, continuous-time Markov chain.
    """
    def __init__(self, stateSpace, EQ, R, brl, nSites, startSeq=[], endSeq=[]):
    #Initializing variables that are necessary for simulating a discrete-time Markov chain
        self.stateSpace = [] # state space
        self.EQ = EQ    #equilibrium freq
        self.R = R      #exchangeabilities
        self.Q = []    Q-matrix
        self.brl = brl #branch length (nIterations, length of branch)
        self.nSites = nSites #number of sites (nChains, one chain per site)
        self.simStates = [] #list of simulated states
        self.waitTime = [] #list to store waiting times
        self.startSeq = startSeq #starting sequence
        self.endSeq = endSeq #ending sequence
        self.likelihood = 1

#Note: EQ and R together make up the Q matrix. In previous version was self.tMatrix = Q, 
#and then in init function included Q as a variable.
# double _ _ are 'special functions' that are not meant to be messed with

    def discSamp(self,states=[],probs=[]):
        """
        Samples from an arbitrary discrete distribution.
        States and probs lists must be equal in length. Probs must sum to 1.
        """
        r = random.random()
        cumulProb = 0
        index = 0
        for p in probs:
            cumulProb = cumulProb + p
            if r < cumulProb:
                return states[index]
            index += 1
        print("ERROR: Probabilities did not add to 1!")

def clear(self):
    """
    Method to clear lists of simulated states and waiting times.
    """
    self.simStates = []
    self.waitTimes = []
    self.likelihood = 1
    

def createQ(self):
    """
    Function fo create Q-matrix from equilibrium frequencines and exchangeabilities
    """
    
    numStates = len(self.stateSpace)
    Q = numpy.matrix(numpy.zeros(shape = (numStates, numStates)))
    rIndex = 0
    for row in range(numStates):                # Rows
        for col in range(numStates):            # Columns
            if (row != col):
                Q[row, col] = self.EQ[col]
    for row in range(numStates):
        for col in range(numStates):
            if(col > row):
            Q[row, col] *= self.R[rIndex]
            rIndex += 1
    for col in range(numStates):                #Reverse
        for row in range(numStates):
            if(col < row):
            Q[row, col] *= self.R[rIndex]
            rIndex += 1
    for state in range(numStates):
        Q[state, state] = 
        

def run(self):
    """
    Method to simulate the states sampled by a Markov chain.
    """
    
    # Reset chains here to empty list of lists
    self.clear()
        
    # For loop across chains (we'll simulate chains one at a time)
    for site in range(self.nsites):
        #Define starting sequence
        if (len(self.startSeq) < site):
            self.startSeq[site] = self.discSamp(self.stateSpace, self.EQ)
        # For loop across iterations for this chain
            #Note: E ^ Q*T, probability matrix, if A prob of TCG

            for iter in range(0,iter):


        
#Here is what I would do if I could figure out how to code it:
        #draw wait time from an exponential distribution
        #rate of the exponential is a function of the transition matrix, dependent on 
        #what state you are currently in
        #plug into exponential, numpy has function to draw from exponential
#numpy.linalg.matrix_power(numpy.matrix(self.tMatrix),self.iter) #matrix to the power 


"""

Part 3: Simulate DNA evolution along a branch under Jukes-Cantor
	- Define a discrete-state (4 nucleotides), continuous-time chain
	- Be sure to normalize Q-matrix (equal nucleotide frequencies)
	- Draw a list of starting nucleotides
	- For each one, simulate evolution along a branch of given length
		- Store character states and waiting times for these simulations
	"""

#Jukes-Cantor
self.matrix = [[-1, 1/3, 1/3, 1/3], [1/3, -1, 1/3, 1/3], [1/3, 1/3, -1, 1/3], [1/3, 1/3, 1/3, -1]]
stateSpace = ['A', 'C', 'T', 'G']
freq = [0.25, 0.25, 0.25, 0.25] #equal prob of each nucleotide

"""
Part 4: Generalize the Jukes-Cantor model to simulate under GTR. Verify that the simulation
	is working properly by:
	- Comparing forward and reverse probabilities for simulated histories
	- Simulate along very long branches to ensure that state frequencies match expectations
	- Compare the average number of changes to the expected branch length
	"""

#GTR
self.matrix = #I know this matrix is supposed to be variable (Q matrix is dependent on
#pie and r variables, but I'm not sure how avoid "hard coding" the values into the model.
stateSpace =['A', 'C', 'T', 'G']
freq = [0.25, 0.25, 0.25, 0.25] #equal prob of each nucleotide

#For GTR you need to draw from a rate distribution, unlike Jukes-Cantor which is
#a fixed value

"""
Ok so I've spent a long, long time trying to figure out how to do this assignment and I 
still don't feel the slightest bit close to understanding how to implement. I feel like
I get the theory behind sequence evolution, continuous uses a 'waiting time', branch 
lengths are number of substitutions which depend on the values in the Q rate matrix etc.
But I do not at all get the object oriented programming nor all the .linalg, .index type
commands which are new for this assignment. I am posting assignment 4 knowing it is no 
where close to being complete, but hopefully it will help you figure out where we are 
stuck, given that the next assignment is supposed to build on this one. Help!?
"""

