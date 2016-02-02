from hand import hand
import random

def main():
    # variables to play around with
    populationSize = 200
    generations = 2
    parents = 100

    # loop through generations
    for gen in range(generations):
        population = []

        # STEP 1: Generate population
        for i in range(populationSize):
            population.append(hand())

        # STEP 2: Calculate fitness of each hand and average population fitness
        calculatePopulationFitness(population, populationSize, gen)

        # STEP 3: Select parents for next generation
        # sort by fitness
        population.sort(key=lambda hand: hand.fitness, reverse=True)
        # create spinner
        spinner = createSpinner(population)
        # choose parents

# Create and return a "spinner"
def createSpinner(population):
    spinner = []
    start = 0
    for hand in population:
        fitness = hand.fitness
        spinner.append((start, start + fitness, hand))
        start += fitness
    return spinner

def selectParents(spinner, phi):
    step = 1/phi

def binSearch(wheel, num):
    mid = len(wheel)//2
    low, high, answer = wheel[mid]
    if low<=num<=high:
        return answer
    elif low > num:
        return binSearch(wheel[mid+1:], num)
    else:
        return binSearch(wheel[:mid], num)

def select(wheel, N):
    stepSize = 1.0/N
    answer = []
    r = random.random()
    answer.append(binSearch(wheel, r))
    while len(answer) < N:
        r += stepSize
        if r>1:
            r %= 1
        answer.append(binSearch(wheel, r))
    return answer

# Calculate the fitness of each hand in the population
# Calculate and print average fitness of the population
# Determine and print the hand that has the maximum fitness
def calculatePopulationFitness(population, populationSize, gen):
    fitnessAvg = 0
    currScore = 0
    maxFitness = 0
    maxFitnessHand = population[0]
    for currentHand in population:
        currScore = currentHand.calculateFitness()
        fitnessAvg += currScore
        if currScore > maxFitness:
            maxFitness = currScore
            maxFitnessHand = currentHand
    fitnessAvg = fitnessAvg / populationSize
    print 'Fitness Score for Generation #' + str(gen) + ' = ' + str(fitnessAvg)
    print '    Maximum fitness is ' + str(maxFitness) + " for the hand " + maxFitnessHand.__str__()

main()
