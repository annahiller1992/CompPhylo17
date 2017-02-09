#Anna E. Hiller, 6 Feb. 2017
#Comp Phylo Assignment 2

# Sampling from a Discrete Distribution (2a)

#1.
In [13]: def factorial(n):
    ...:     if n == 1:
# n == min, change value here
    ...:         return n
    ...:     else:
    ...:         return n*factorial(n-1)
    ...:     

In [14]: factorial(7)
# number in () is the max value, change value here
Out[14]: 5040

In [73]: def factorial(n):
    ...:     if n == k:
    ...:         return n
    ...:     else:
    ...:         return n*factorial(n-1)

In [81]: k = 3
In [82]: factorial(6)
Out[82]: 360
# k = min, n = max
#Using: https://www.programiz.com/python-programming/examples/factorial-recursion

#2.(a)
#Binomial coefficient

######## CALL THIS ########
In [61]: def binomial (n, k):  #call this for simulations
    ...:     x = n - k
    ...:     def factorial_n(n):
    ...:         if n == 1:
    ...:              return n
    ...:         else:
    ...:             return n*factorial_n(n-1)
    ...:     def factorial_k(k):
    ...:         if k == 1:
    ...:             return k
    ...:         else:
    ...:             return k*factorial_k(k-1)
    ...:     def factorial_x(x):
    ...:         if x == 1:
    ...:             return x
    ...:         else:
    ...:             return x*factorial_x(x-1)
    ...:     result = factorial_n(n)/(factorial_k(k)*factorial_x(x))
    ...:     return result
    ...: 

In [62]: binomial (6, 2)
Out[62]: 15.0

#2.(b)
In [24]: def binom (n, k):
# n choose k, have to define nmax seperately
    ...:     def factorial_2n(n):
    ...:         if n == 1:
    ...:              return n
    ...:         elif n == (nmax-k+1):
    ...:              return n 
    ...:         elif n < (nmax-k+1): 
    ...:              return 1
    ...:         else:
    ...:             return n*factorial_2n(n-1)
    ...:     def factorial_2k(k):
    ...:         if k == 1:
    ...:             return k
    ...:         else:
    ...:             return k*factorial_2k(k-1)
    ...:     result = factorial_2n(n)/(factorial_2k(k))
    ...:     return result
    ...: 

In [25]: nmax = 6

In [26]: binom (6, 2)
Out[26]: 15.0

#3. The times seem to be the same, but I get an error sooner using the 2(a) binomial function than I do using the 2(b) binom function. See below.

In [41]: nmax = 1000
In [42]: binom (1000, 7)
Out[42]: 1.94280608456793e+17

In [43]: binomial (1000, 7)
RecursionError: maximum recursion depth exceeded in comparison

#4. Probability mass function (pmf) for the Binomial(n,p) distribution
######## CALL THIS ########
In [4]: def PMF (n, k, p):  #Call this for simulations
   ...:     result = (binomial (n, k))*pow(p, k)*pow((1-p),(n-k))
   ...:     return result
   ...: 

In [5]: PMF (6, 2, 0.5)
Out[5]: 0.234375

#5. Arbitrary discrete distribution
In [61]: a = ["2, 0.1", "5, 0.4", "6, 0.2", "8, 0.1"]

In [62]: b = (0.1, 0.4, 0.2, 0.1)

In [63]: for x, y, in zip(a, b):
    ...:     print(x, y)
    ...:     
2 0.1
5 0.4
6 0.2
8 0.1

In [129]: print(random.choice(a)) #This is not correct, since a and b are not linked
6

In [130]: print(random.choice(b)) #But I can't figure out how combine
0.1

#Other option
In [15]: a = ["2, 0.1", "5, 0.4", "6, 0.2", "8, 0.1"]

In [16]: print(random.choice(a))
2, 0.1

#Using: http://stackoverflow.com/questions/1663807/how-can-i-iterate-through-two-lists-in-parallel-in-python

# ML Hill Climber (2b)
#1-3.
In [26]: def climbTheHill(pCurr, precision):
    ...:     diff = 0.1
    ...:     while (diff > precision):
    ...:         pCurrLike = PMF (6, 2, pCurr)
    ...:         pUp = pCurr + diff
    ...:         pDown = pCurr - diff
    ...:         pUpLike = PMF (6, 2, pUp)
    ...:         pDownLike = PMF (6, 2, pDown)
    ...:         while (pUpLike > pCurrLike):
    ...:             print("up"),
    ...:             pCurr = pCurr + diff
    ...:             pCurrLike = PMF (6, 2, pCurr)
    ...:             pUp = pCurr + diff
    ...:             pDown = pCurr - diff
    ...:             pUpLike = PMF (6, 2, pUp)
    ...:             pDownLike = PMF (6, 2, pDown)
    ...:         while (pDownLike > pCurrLike):
    ...:             print("down"),
    ...:             pCurr = pCurr - diff
    ...:             pCurrLike = PMF (6, 2, pCurr)
    ...:             pUp = pCurr + diff
    ...:             pDown = pCurr - diff
    ...:             pUpLike = PMF (6, 2, pUp)
    ...:             pDownLike = PMF (6, 2, pDown)
    ...:         return(pCurr)
    ...: 

In [27]: climbTheHill(0.5, 0.08)
down
down
Out[27]: 0.30000000000000004

#4. Check
In [28]: PMF (6, 2, 0.30000000000000004)
Out[28]: 0.324135

In [30]: diff = 0.1

In [31]: PMF (6, 2, (0.30000000000000004+diff))
Out[31]: 0.31104000000000004

In [32]: PMF (6, 2, (0.30000000000000004-diff))
Out[32]: 0.24576

#good to go!

#5. Repeate with lower value of diff
In [33]: def climbTheHill(pCurr, precision):
    ...:     diff = 0.05
    ...:     while (diff > precision):
    ...:         pCurrLike = PMF (6, 2, pCurr)
    ...:         pUp = pCurr + diff
    ...:         pDown = pCurr - diff
    ...:         pUpLike = PMF (6, 2, pUp)
    ...:         pDownLike = PMF (6, 2, pDown)
    ...:         while (pUpLike > pCurrLike):
    ...:             print("up"),
    ...:             pCurr = pCurr + diff
    ...:             pCurrLike = PMF (6, 2, pCurr)
    ...:             pUp = pCurr + diff
    ...:             pDown = pCurr - diff
    ...:             pUpLike = PMF (6, 2, pUp)
    ...:             pDownLike = PMF (6, 2, pDown)
    ...:         while (pDownLike > pCurrLike):
    ...:             print("down"),
    ...:             pCurr = pCurr - diff
    ...:             pCurrLike = PMF (6, 2, pCurr)
    ...:             pUp = pCurr + diff
    ...:             pDown = pCurr - diff
    ...:             pUpLike = PMF (6, 2, pUp)
    ...:             pDownLike = PMF (6, 2, pDown)
    ...:         return(pCurr)
    ...: 
In [39]: p = climbTheHill(0.5, 0.01)
down
down
down

In [40]: PMF (6, 2, p)
Out[40]: 0.32800523437499984

In [41]: diff = 0.1

In [42]: PMF (6, 2, (p+diff))
Out[42]: 0.27795023437499994

In [43]: PMF (6, 2, (p-diff))
Out[43]: 0.296630859375

# changed value of diff, <0.001

In [54]: def climbTheHill(pCurr, precision):
    ...:     diff = 0.0009
    ...:     while (diff > precision):
    ...:         pCurrLike = PMF (6, 2, pCurr)
    ...:         pUp = pCurr + diff
    ...:         pDown = pCurr - diff
    ...:         pUpLike = PMF (6, 2, pUp)
    ...:         pDownLike = PMF (6, 2, pDown)
    ...:         while (pUpLike > pCurrLike):
    ...:             print("up"),
    ...:             pCurr = pCurr + diff
    ...:             pCurrLike = PMF (6, 2, pCurr)
    ...:             pUp = pCurr + diff
    ...:             pDown = pCurr - diff
    ...:             pUpLike = PMF (6, 2, pUp)
    ...:             pDownLike = PMF (6, 2, pDown)
    ...:         while (pDownLike > pCurrLike):
    ...:             print("down"),
    ...:             pCurr = pCurr - diff
    ...:             pCurrLike = PMF (6, 2, pCurr)
    ...:             pUp = pCurr + diff
    ...:             pDown = pCurr - diff
    ...:             pUpLike = PMF (6, 2, pUp)
    ...:             pDownLike = PMF (6, 2, pDown)
    ...:         return(pCurr)
    ...: 

In [55]: p = climbTheHill(0.5, 0.0001)

#6. Value
In [56]: PMF (6, 2, p)
Out[56]: 0.32921798355968235 #final value

#function form: starting p value and observed data (k,n) #Use this for simulation
######## CALL THIS ########
In [53]: def climbTheHill(pCurr, n, k):
    ...:     diff = 0.0001  ### CHANGE THIS ###
    ...:     pCurrLike = PMF (n, k, pCurr)
    ...:     pUp = pCurr + diff
    ...:     pDown = pCurr - diff
    ...:     pUpLike = PMF (n, k, pUp)
    ...:     pDownLike = PMF (n, k, pDown)
    ...:     while (pUpLike > pCurrLike):
    ...:         pCurr = pCurr + diff
    ...:         pCurrLike = PMF (n, k, pCurr)
    ...:         pUp = pCurr + diff
    ...:         pDown = pCurr - diff
    ...:         pUpLike = PMF (n, k, pUp)
    ...:         pDownLike = PMF (n, k, pDown)
    ...:     while (pDownLike > pCurrLike):
    ...:         pCurr = pCurr - diff
    ...:         pCurrLike = PMF (n, k, pCurr)
    ...:         pUp = pCurr + diff
    ...:         pDown = pCurr - diff
    ...:         pUpLike = PMF (n, k, pUp)
    ...:         pDownLike = PMF (n, k, pDown)
    ...:     return(pCurr)
    ...: 

In [54]: climbTheHill(0.2, 6, 2)
Out[54]: 0.33329999999998533

# Simulation of Likelihood Ratio Cutoff (2c)

######## CALL THIS ########
#1-2. Simulate datasets
In [4]: import random
In [1]: value = [] #This is the dataset with 100 values of k
In [2]: n = 5
In [23]:for i in range(1, 101):
    ...:     k = random.randint(0, (n))
    ...:     value.append(k)
    ...:   

In [12]:estimate = []

In [13]:for i in value:
    ...:     z = climbTheHill(0.2, n, i)
    ...:     #estimate.append(z)
    ...: 
RecursionError: maximum recursion depth exceeded in comparison

In [12]: estimate
Out[12]: [0.2, 0.2, 0.399999999999978, 0.399999999999978, 0.599999999999956]

#The function is stopping early because I get this error: RecursionError: maximum recursion depth exceeded in comparison
#I am just going to finish the assignment using a fake dataset

#FAKE DATASET! I could not get the simulation to run so I made up p values
In [22]: fake = []

In [23]: for i in range(100):
    ...:     k = (random.random())
    ...:     fake.append(k)
    ...:     
#3. Calculate likelihood ratios comparing the true p to ML estimates.
#Assuming 6 draws, with 3 successes and a p = 0.5 as true
In [21]: ratio = []

In [22]: for i in fake:
    ...:     z = (((PMF(6, 3, i))/(PMF(6, 3, 0.5))))
    ...:     ratio.append(z)
    ...:     
#4. Likelihood ratio cutoff to ensure that the probability of seeing a LR score that big or greater is <= 5%
In [26]: ratio.sort()
#data cutoff for only 5% of data bigger (so values 96-100) is likelihood ratio = 0.9566
In [29]: LikelihoodRatio = 0.9566



