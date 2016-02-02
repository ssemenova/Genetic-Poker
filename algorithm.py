from hand import hand
import random

def main():
    population = []

    # generate population of 200 hands
    for i in range(1):
        population.append(hand())

    # for each hand, calculate its fitness
    for currentHand in population:
        currentHand.calculateFitness()

    # mutate = random.randrange(1,10) == 1
    # if mutate:
    #     mutate(population[i])


main()
