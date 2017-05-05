####################
# Phylogenetics    #
# Final Assignment #
# Anna E. Hiller   #
# May 5th 2017     #
####################

#start RB
cd Documents/Classes/Phylogenetics/RevBayes/
./rb

######## CODE #########

#######################
# Reading in the Data #
#######################

#load data
data <- readDiscreteCharacterData("data/Diglossa.nex")

#retrieve dataset info
n_species <- data.ntaxa()
taxa <- data.taxa()

#set my move index, counter variable for number of moves made, starts at 0
mvi = 0
mni = 0
#NOTE: this is where the pdf tutorial went wrong, it never had mni defined

######################
# Substitution Model #
######################

#specify the GTR+G (general time reversible) substitution model 
#applied uniformly to all sites
er_prior <- v(1,1,1,1,1,1)
er ~ dnDirichlet(er_prior)
moves[++mvi] = mvSimplexElementScale(er,weight=3)
pi_prior <- v(1,1,1,1) 
pi ~ dnDirichlet(pi_prior)
moves[++mvi] = mvSimplexElementScale(pi,weight=2)
#create a deterministic variable for the GTR rate matrix
Q := fnGTR(er,pi) 


#############################
# Among Site Rate Variation #
#############################

#set up gamma distribution model of rate variation among sites
#create constant nodes
alpha_prior_mean <- 5.0
alpha_prior_sd <- 0.587405
#create stochastic nodes
alpha ~ dnLognormal( alpha_prior_mean, alpha_prior_sd )
#create deterministic node, vector that will hold the set of k rates 
#drawn from the gamma distribution with k rate categories
gamma_rates := fnDiscretizeGamma( alpha, alpha, 4, false )

#random variable that controls the rate variation is the stochastic node alpha
#apply a scale move to this parameter
#add moves for the stationary frequencies, exchangeability rates and the shape parameter
moves[++mvi] = mvScale(alpha,weight=2)


##############
# Tree model #
##############

#The tree (the topology and node ages) is a stochastic node in our phylogenetic model.
#Constant-rate birth-death process as the prior distribution on the tree.
#The distribution in RevBayes is dnBDP().
#For the birth-death process we need a speciation rate and extinction rate parameter.
#Instead of prior distributions on these parameters directly, we will specify
#lognormal prior distributions on the diversification and turnover rates.

#the birth rate is a stochastic random variable drawn from a lognormal prior
#MCMC samples this variable using a scale proposal
diversification_mean <- ln( ln(n_species/2.0) / 90 )
diversification_sd <- 0.587405*2
diversification ~ dnLognormal(mean=diversification_mean,sd=diversification_sd) 
moves[++mvi] = mvScale(diversification,lambda=1.0,tune=true,weight=3.0)

turnover_mean <- ln( ln(n_species/2.0) / 90 )
turnover_sd <- 0.587405*2
turnover ~ dnLognormal(mean=turnover_mean,sd=turnover_sd) 
moves[++mvi] = mvScale(turnover,lambda=1.0,tune=true,weight=3.0)

#Transform the parameters
birth_rate := diversification + turnover
death_rate := turnover

#rho is the probability of sampling species at the present
#fix this to 6/18, since there are 18 described species of Diglossa
#and we have sampled 6 (two species have 2 representatives sampled)
rho <- n_species/18

#truncate the normal distribution, to give positive real number (root age is >0)
#BDP is conditioned on the root time, here we use an informative prior on the root age
#this prior is a normal distribution with mean 90 and standard deviation of 6
root_time ~ dnNormal(mean=10.1,sd=6.3,min=0.0,max=1000.0)
#dates in the above informative prior come from Mauck and Burns 2009, Biol J Linnean Soc
#10.1mya 7.2–13.4 95% interval
#worked backwards to calculate the SD: 1.96*(SD/4) = 3.1
#4 is the square root of the sample size, 16 tips so 4
#SD = 6.33
#I also changed the max to 1000 mya because this is a more recent split than the 
#primates example (used 5000 mya)
moves[++mvi] = mvScale(root_time, weight=2.0)

#the time tree is a stochastic node modeled by the constant rate birth-death process (dnBDP)
psi ~ dnBDP(lambda=birth_rate, mu=death_rate, rho=rho, rootAge=root_time, samplingStrategy="uniform", condition="survival", taxa=taxa)

#add some moves that change the tree, propose different moves to explore parameter space
moves[++mvi] = mvNarrow(psi, weight=5.0)
moves[++mvi] = mvNNI(psi, weight=1.0)
moves[++mvi] = mvFNPR(psi, weight=3.0)
moves[++mvi] = mvGPR(psi, weight=1.0)
moves[++mvi] = mvSubtreeScale(psi, weight=3.0)
moves[++mvi] = mvNodeTimeSlideUniform(psi, weight=15.0)

#Option 1: look into the generated maximum a posteriori tree in FigTree.
#Option 2: add deterministic variables for the ages that you are interested in 
#and look at the values in Tracer.

#add a deterministic variable for the age of
#Diglossa carbonaria superspecies
clade_carbonaria = clade("Diglossa_carbonaria", "Diglossa_humeralis", "Diglossa_brunneiventris_AMNH", "Diglossa_brunneiventris_FMNH")
age_carbonaria := tmrca(psi, clade_carbonaria)

#Diglossa lafresnayii superspecies
clade_lafresnayii = clade("Diglossa_lafresnayii", "Diglossa_gloriosissima")
age_lafresnayii := tmrca(psi, clade_lafresnayii)


###################
# PhyloCTMC Model #
###################

#Global Molecular Clock Model
logClockRate ~ dnUniform(-6,1)
clockRate := 10^logClockRate
moves[++mvi] = mvSlide(logClockRate)

#Putting it all together
# the sequence evolution model
seq ~ dnPhyloCTMC(tree=psi, Q=Q, branchRates=clockRate, siteRates=gamma_rates, type="DNA")
# attach the data
seq.clamp(data)


#############
# THE Model #
#############

# We define our model.
# We can use any node of our model as a handle, here we chose to use the rate matrix.
mymodel = model(Q)

#Specifying monitors
monitors[++mni] = mnModel(filename="output/Diglossa_root_calibration_prior.log",printgen=10, separator = TAB)
monitors[++mni] = mnFile(filename="output/Diglossa_root_calibration_prior.trees",printgen=10, separator = TAB, psi)
monitors[++mni] = mnScreen(printgen=1000, clockRate, root_time, age_lafresnayii)

#Initializing and Running
#create MCMC object
mymcmc = mcmcmc(mymodel, monitors, moves, nruns = 2, nchains = 2)
#originally used 4 chains but that took waaaaaaaay too long
#NOTE: to use multiple chains add in a third 'mc' before the (

#burnin
mymcmc.burnin(generations=10000,tuningInterval=250)
#run
mymcmc.run(generations=30000)
#Look at the file called output/Diglossa_root_calibration.log in Tracer.

# Now, we will analyze the tree output.
# Let us start by reading in the tree trace
treetrace = readTreeTrace("output/Diglossa_root_calibration_prior.trees", treetype="clock")
map_tree = mapTree(treetrace,"output/Diglossa_root_calibration_prior.trees")