import random

class hand(object) :
    # a hand of cards is defined as a list of tuples
    # where the first is the number of the card (1 - 13)
    # and the second is the suit
    # instantiating a hand object will automatically generate a hand
    def __init__( self ) :
        # self.cards = self.__generateHand()
        self.cards = [[2,1], [2,1], [2,1], [2,1], [1,1]]
        self.fitness = []

    def __str__( self ) :
       returnString = ""
       for card in self.cards:
           returnString += str(card) + " "
       return returnString

    # generates a hand, checks legality, returns
    def __generateHand( self ):
        newHand = []
        # generate 5 random hands
        # includes check for no duplicates, because you can't have duplicate cards in a deck
        for i in range(5):
            newHand.append(self.__generateCard())
        # check legality of current hand
        newHand = self.fixLegality(newHand)
        return newHand

    # generates a card
    # which is just a tuple of two random numbers
    # (cardType, suit)
    # returns the card
    def __generateCard( self ):
        cardType = random.randrange(1,13)
        suit = random.randrange(1,4)
        return [cardType, suit]

    # checks legality of a hand of cards and fixes a hand if it isn't legal
    # returns fixed new hand
    def fixLegality( self, oldHand ):
        newHand = []
        # for each card in the old hand,
        # either add the card to the new hand
        # or generate a new card and add that to the new hand
        for card in oldHand:
            while card in newHand:
                card = self.__generateCard()
            newHand.append(card)
        return newHand

    def calculateFitness( self ):
        # since a poker hand's type is the highest possible type it could be
        # we're just going to test for the different kinds of hands starting from the best to the worst

        # ROYAL FLUSH
        # sort the cards by card type
        # if card type order is 1, 10, 11, 12, 13, then we have a royal flush
        self.cards.sort()
        if (self.cards[0][0] == 1 and
            self.cards[1][0] == 10 and
            self.cards[2][0] == 11 and
            self.cards[3][0] == 12 and
            self.cards[4][0] == 13):
            return 1000

        # FOUR OF A KIND
        # cards are already sorted by card type
        # if card type order is the same four times in a row then it is a four of a kind
        prevCardType = self.cards[0][0]
        count = 0
        for cardType, suit in self.cards:
            if cardType == prevCardType:
                count += 1
            else:
                prevCardType = cardType
        if count == 4: return 800

        # STRAIGHT FLUSH
        # cards are already sorted by type
        # if cards are in numerical order and identical suits, then straight flush
        prevCardType = self.cards[0][0]
        prevSuit = self.cards[0][1]
        count = 0
        for cardType, suit in self.cards:
            if suit == prevSuit and cardType == prevCardType + 1:
                count += 1



        # FULL HOUSE
        # FLUSH
        # STRAIGHT
        # THREE OF A KIND
        # TWO PAIR
        # PAIR
