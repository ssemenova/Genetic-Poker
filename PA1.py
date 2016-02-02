from hand import hand
import random

def main():
    population = []

    # generate population of 200 hands
    for i in range(2):
        population.append(hand(generateHand()))

    fitnessList = calculateFitnessList(population)

    # mutate = random.randrange(1,10) == 1
    # if mutate:
    #     mutate(population[i])


# generates and returns a legal hand
def generateHand():
    currentHand = []
    # generate 5 random hands
    # includes check for no duplicates, because you can't have duplicate cards in a deck
    for i in range(5):
        currentHand.append(generateCard())
    # check legality of current hand, if not legal then change cards so it is
    currentHand = legal(currentHand)
    return currentHand

# generates a card
# which is just a tuple of two numbers
# (cardType, suit)
# returns the card
def generateCard():
    cardType = random.randrange(1,13)
    suit = random.randrange(1,4)
    return (cardType, suit)

# checks legality of a hand of cards and returns a legal hand
def legal(oldHand):
    newHand = []
    # for each card in the old hand,
    # either add the card to the new hand
    # or generate a new card and add that to the new hand
    for card in oldHand:
        while card in newHand:
            card = generateCard()
        newHand.append(card)
    return newHand

def calculateFitnessList(population):
    fitnessList = []

    for hand in population:
        fitnessList.append(calculateFitnessOfHand(hand))

def calculateFitnessOfHand(hand):
    # royal flush
    sortedHand = hand.sort()


    # four of a kind
    # straight flush
    # full house
    # flush
    # straight
    # three of a kind
    # two pair
    # pair

main()
