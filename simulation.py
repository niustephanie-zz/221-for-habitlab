import random
import numpy as np
import datetime

# Main function. 
def simulate():
	users = range(10)
	interventions = ["minute watch", "supervisor", "side kicker", "think twice", "no comment", "bouncer"]
	allProbs = []
	for u in users:
		allProbs.append(generateProbs(len(interventions)))
	times = []
	for u in users:
		times.append(generateTimes(allProbs[u], interventions, 50))
		
	# sanity check
	# print "BASE", generateBaseTime(50)
	# for i in interventions:
	# 	print np.mean(times[0][i])
	# print allProbs[0]

	for u in users:
		getBaseTimeSaved(u, times[u], interventions)

def getBaseTimeSaved(ID, times, interventions):
	print "USER: ", ID
	base = generateBaseTime(50)
	for i in interventions:
		saved = base - np.mean(times[i])
		if saved < 0:
			saved = 0
		print "time saved for", i, ":", saved

# Returns a map of interventions to array of times per session
# generated using a specific user's probability distribution. 
def generateBaseTime(iters):
	random.seed(datetime.datetime.now().time())
	base = 0.0
	for _ in range(iters):
		base = base + (random.random() + 0.1) * 5000
	return base/iters

# Returns a map of interventions to array of times per session
# generated using a specific user's probability distribution. 
def generateTimes(probs, interventions, iters):
	random.seed(datetime.datetime.now().time())
	times = {}
	for i in interventions:
		times[i] = []
	for _ in range(iters):
		curr = random.randrange(len(interventions))
		seshTime = (random.random() + 0.1) * (probs[curr] * 6) * 5000
		times[interventions[curr]].append(seshTime)
	return times
	
# Returns a list the length of the number of interventions
# containing probabilities that sum to 1. 
def generateProbs(size):
	random.seed(datetime.datetime.now().time())
	probs = []
	sum = 0.0
	for _ in range(size):
		curr = random.random()
		probs.append(curr)
		sum = sum + curr
	for i in range(len(probs)):
		probs[i] = probs[i]/sum
	newSum = 0.0
	return probs

simulate()
