from hand import hand
import random

def main():
    # loop through generations
    for gen in range(200):
        population = []

        # Step 1: generate population of 200 hands
        for i in range(200):
            population.append(hand())

        # Step 2: for each hand, calculate its fitness
        fitnessList = []
        fitnessAvg = 0
        currScore = 0

        for currentHand in population:
            currScore = currentHand.calculateFitness()
            fitnessList.append(currScore)
            fitnessAvg += currScore

        fitnessAvg = fitnessAvg / 200
        print 'Fitness Score for generation ' + str(gen) + ' = ' + str(fitnessAvg)


        # mutate = random.randrange(1,10) == 1
        # if mutate:
        #     mutate(population[i])


main()
