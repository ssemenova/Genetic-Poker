from __future__ import division # floating point division instead of integer division, which is the default in python 2
from hand import hand
from numpy.random import choice # used to make a weighted random choice for parents
import random # random number generator
import copy # create copy of object

def main():
    # variables to play around with
    populationSize = 200
    generations = 300
    numParents = int(populationSize / 2)

    # STEP 1: Generate population
    population = []
    for i in range(populationSize):
        population.append(hand())

    # loop through generations
    for gen in range(generations):
        # STEP 2: Calculate fitness of each hand and average population fitness
        probabilityList = calculatePopulationFitness(population, populationSize, gen)

        # STEP 3: Select parents for next generation
        # sort in reverse order of fitness
        population.sort(key=lambda hand: hand.fitness, reverse=True)
        # choose parents
        parents = []
        for i in range(numParents):
            # choose random parent, giving weight to their fitness
            newParent = choice(population, p = probabilityList)
            parents.append(newParent)

        # STEP 4: Reproduce with 80% crossover, 10% mutation, and 10% elitism
        # new population becomes the result of reproduction
        # start with no children
        population = []
        # mutation 10% of the time:
        # creating .1 * populationSize children
        for i in range(int(.1 * populationSize)):
            population.append(mutate(parents))

        # elitism 10% of the time:
        for i in range(int(.1 * populationSize) - 1):
            population.append(elitism(parents))

        # crossover 80%
        for i in range(int(.8 * populationSize)):
            population.append(crossover(parents))

    print "Final generation"
    calculatePopulationFitness(population, populationSize, generations)

# Calculate the fitness of each hand in the population
# Calculate and print average fitness of the population
# Determine and print the hand that has the maximum fitness
def calculatePopulationFitness(population, populationSize, gen):
    maxFitness = 0 # maximum fitness of a hand
    maxFitnessHand = population[0] # hand that has the maximum fitness
    oddsList = [] # list of probabilities associated with a hand .. needed to make the choice of parents

    for currentHand in population:
        currScore = currentHand.calculateFitness()
        oddsList.append(currScore)
        if currScore > maxFitness:
            maxFitness = currScore
            maxFitnessHand = currentHand

    totalFitness = sum(oddsList)

    # scaling probabilities so they all add up to one
    sum2 = 0
    probabilityList = [float(i)/totalFitness for i in oddsList]
    probabilityList.sort(reverse=True)

    print 'Fitness Score for Generation #' + str(gen) + ' = ' + str(totalFitness / populationSize)
    print '    Maximum fitness is ' + str(maxFitness) + " for the hand " + maxFitnessHand.__str__()

    return probabilityList

# mutates a child from a random parent
def mutate(parents):
    # pick random parent
    parent = parents[random.randrange(1, len(parents))]
    # copy parent's information to the child
    child = copy.deepcopy(parent)
    # mutate the child
    child.mutate()
    return child

# creates a child that is a clone of the parent
def elitism(parents):
    # pick random parent
    parent = parents[random.randrange(1, len(parents))]
    # copy parent's information to child
    child = copy.deepcopy(parent)
    return child

# creates a child that is a combination of both parents
def crossover(parents):
    legal = False
    while not legal:
        # pick two random parents
        parent1 = parents[random.randrange(1, len(parents))]
        parent2 = parents[random.randrange(1, len(parents))]
        index = random.randrange(0,4)
        child = hand(parent1.cards[0:index] + parent2.cards[index:5])
        legal = child.checkLegality(child.cards)
    return child

main()
