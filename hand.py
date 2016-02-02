import random

class hand( object ) :
    # a hand of cards is defined as a list of tuples
    # where the first is the number of the card (1 - 13)
    # and the second is the suit
    # instantiating a hand object will automatically generate a hand
    def __init__( self ) :
        # self.cards = self.__generateHand()
        self.cards = self.__generateHand()
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

    # calculates a fitness score for the hand, saves it to the fitness variable, and returns the #
    def calculateFitness( self ):
        # since a poker hand's type is the highest possible type it could be
        # we're just going to test for the different kinds of hands starting from the best to the worst

        # sort the cards by card type
        self.cards.sort()

        # ROYAL FLUSH
        # if card type order is 1, 10, 11, 12, 13,
        if (self.cards[0][0] == 1 and
            self.cards[1][0] == 10 and
            self.cards[2][0] == 11 and
            self.cards[3][0] == 12 and
            self.cards[4][0] == 13):
            self.fitness = 90
            return 90

        # FOUR OF A KIND
        # if card type order is the same four times in a row
        prevCardType = self.cards[0][0]
        count = 0
        for cardType, suit in self.cards:
            if cardType == prevCardType:
                count += 1
            else:
                prevCardType = cardType
                count = 0
        if count == 4:
            self.fitness = 90
            return 80

        # STRAIGHT FLUSH
        # if cards are in numerical order and identical suits
        prevCardType = self.cards[0][0]
        prevSuit = self.cards[0][1]
        count = 0
        for cardType, suit in self.cards:
            if suit == prevSuit and cardType == prevCardType + 1:
                count += 1
                prevCardType = cardType
        if count == 4:
            self.fitness = 70
            return 70

        # FULL HOUSE
        # if three cards of same rank, two of a different matching rank
        checkCardType = self.cards[0][0]
        count = 0
        for cardType, suit in self.cards:
            if cardType == checkCardType:
                count += 1
            if cardType != checkCardType:
                checkCardType = cardType
                count = 1
        if count == 2 or count == 3:
            self.fitness = 60
            return 60

        # FLUSH
        # five cards of the same suit
        cardSuit = self.cards[0][1]
        count = 0
        for cardType, suit in self.cards:
            if suit == cardSuit:
                count += 1
        if count == 5: return 50

        # STRAIGHT
        # five cards in a row, not necessarily matching suit
        prevCardType = self.cards[0][0]
        count = 0
        for cardType, suit in self.cards:
            if cardType == prevCardType + 1:
                count += 1
                prevCardType = cardType
        if count == 4:
            self.fitness = 40
            return 40

        # THREE OF A KIND
        # 3 cards of the same card type
        prevCardType = self.cards[0][0]
        count = 0
        for cardType, suit in self.cards:
            if cardType == prevCardType:
                count += 1
            elif count < 3:
                count = 1
                prevCardType = cardType
        if count == 3:
            self.fitness = 30
            return 30

        # TWO PAIR
        # two pairs of two cards of the same card type
        prevCardType = self.cards[0][0]
        count = 0
        firstPairFound = False
        for cardType, suit in self.cards:
            if cardType == prevCardType:
                count += 1
            elif cardType != prevCardType and count < 2:
                prevCardType = cardType
            elif cardType != prevCardType and count == 2:
                prevCardType = cardType
                firstPairFound = True
        if count > 2 and firstPairFound:
            self.fitness = 20
            return 20

        # PAIR
        # one pair of two cards of the same card type
        prevCardType = self.cards[0][0]
        count = 0
        for cardType, suit in self.cards:
            if cardType == prevCardType:
                count += 1
            elif cardType != prevCardType and count < 2:
                count = 0
        if count == 2:
            self.fitness = 10
            return 10

        # if none of these
        self.fitness = 0
        return 0
