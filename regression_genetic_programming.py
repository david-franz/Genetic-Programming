# fitness function:
# sum of squared area of function vs given points

# https://deap.readthedocs.io/en/master/examples/gp_symbreg.html

from deap import gp, creator, base, tools, algorithms
import deap
import operator
import math
import random
import numpy as np

# decided not to do division or protected division because polynomial approximation

# values of original function
mapping_dictionary = {	-2.00 : 37.00000,
						-1.75 : 24.16016,
						-1.50 : 15.06250,
						-1.25 : 8.91016,
						-1.00 : 5.00000,
						-0.75 : 2.72266,
						-0.50 : 1.56250,
						-0.25 : 1.09766,
						 0.00 : 1.00000,
						 0.25 : 1.03516,
						 0.50 : 1.06250,
						 0.75 : 1.03516, 
						 1.00 : 1.00000,
						 1.25 : 1.09766,
						 1.50 : 1.56250,
						 1.75 : 2.72266,
						 2.00 : 5.00000,
						 2.25 : 8.91016,
						 2.50 : 15.06250,
						 2.75 : 24.16016	}

# generates all the x values we need to assess our function at
float_range_array = np.arange(-2.0, 3.0, 0.25)
float_range_list = list(float_range_array)

def evalSymbReg(individual):
	# Transform the tree expression in a callable function
	func = toolbox.compile(expr=individual)

	# Evaluate the mean squared error between the created function and the given function points
	squared_error = 0
	for x in float_range_array:
		mapping_dictionary[x]
		squared_error += (func(x) - mapping_dictionary[x])**2
	
	return squared_error / len(float_range_list),

if __name__ == '__main__':

	pset = gp.PrimitiveSet("MAIN", 1)
	pset.addPrimitive(operator.add, 2)
	pset.addPrimitive(operator.sub, 2)
	pset.addPrimitive(operator.mul, 2)
	#pset.addPrimitive(protectedDiv, 2)
	pset.addPrimitive(operator.neg, 1)
	pset.addEphemeralConstant("rand101", lambda: random.randint(-1,1))
	pset.renameArguments(ARG0="x")
	pset.renameArguments(ARG1="y")

	creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
	creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

	toolbox = base.Toolbox()
	toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
	toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
	toolbox.register("population", tools.initRepeat, list, toolbox.individual)
	toolbox.register("compile", gp.compile, pset=pset)

	toolbox.register("evaluate", evalSymbReg)
	toolbox.register("select", tools.selTournament, tournsize=3)
	toolbox.register("mate", gp.cxOnePoint)
	toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
	toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)
	
	toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=7))
	toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=7))

	stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
	stats_size = tools.Statistics(len)
	mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
	mstats.register("avg", np.mean)
	mstats.register("std", np.std)
	mstats.register("min", np.min)
	mstats.register("max", np.max)

	pop = toolbox.population(n=300)
	hof = tools.HallOfFame(1)

	pop, log = algorithms.eaSimple(pop, toolbox, 0.5, 0.1, 40, stats=mstats, halloffame=hof, verbose=True)

	print("{}\n".format(hof[0]))