# CS221 Final Project: HabitLab Interventions

# Our oracle is a recommender that knows how much time the user will spend on the current site 
# for each possible intervention (knows the future exactly). 
# The recommender then just returns the intervention with the minimum time that will be spent. 

def recommend(state, interventions, currHistory, allHistory):
	time, user, site = state
	timeSpent = getTimeSpent(user, site, interventions)
    minTime = float('inf')
    minIntervention = interventions[0]
    for i in range(len(timeSpent)):
    	if timeSpent[i] < minTime:
        	minTime = timeSpent[i]
            minIntervention = i
	return minIntervention