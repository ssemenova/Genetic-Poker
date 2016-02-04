import random

class hand( object ) :
    # a hand of cards is defined as a list of tuples
    # where the first is the number of the card (1 - 13)
    # and the second is the suit
    # instantiating a hand object will automatically generate a hand
    def __init__( self, cards = None ) :
        if cards is None:
            self.cards = self.__generateHand()
        else:
            self.cards = cards
        # array of what hand receives which fitness score
        # removed from the rest of the code so I can tweak it easily
        self.fitnessScoreDistribution = [100, 90, 80, 70, 60, 50, 45, 40, 35, 30]
        self.fitness = self.fitnessScoreDistribution[9]

    def __str__( self ) :
       returnString = ""
       for card in self.cards:
           returnString += str(card) + " "
       return returnString

    # generates a legal hand, returns
    def __generateHand( self ):
        newHand = []
        # generate 5 random hands
        # includes check for no duplicates, because you can't have duplicate cards in a deck
        for i in range(5):
            newHand.append(self.__generateCard())
            while not self.checkLegality(newHand):
                newHand[i] = self.__generateCard()
        return newHand

    # generates a card
    # which is just a tuple of two random numbers
    # (cardType, suit)
    # returns the card
    def __generateCard( self ):
        cardType = random.randrange(1,14)
        suit = random.randrange(1,5)
        return [cardType, suit]

    # returns if a hand is legal or not
    def checkLegality( self, oldHand ):
        # print oldHand
        # print 'stuck'
        newHand = []
        for card in oldHand:
            if card in newHand:
                return False
            else:
                newHand.append(card)
        return True

    # mutates a hand by changing one of the cards
    # maintains legality
    def mutate( self ):
        legal = False
        # mutate index selects which card to mutate randomly
        mutateIndex = random.randrange(0,5)
        # typeOrSuit selects whether the type or suit should be changed
        typeOrSuit = random.randrange(0,2) # 0 = type, 1 = suit
        while not legal:
            # addOrSubtract selects whether to add or subtract the cardType or suit
            addOrSubtract = random.randrange(0,2) # 0 = add, 1 = subtract
            # amountToMutate is the amount that is added or subtracted
            amountToMutate = random.randrange(1,5)

            mutatedCard = self.cards[mutateIndex][typeOrSuit]

            if addOrSubtract == 0:
                # some math trickery so if we try to make a card number 15, it'll wrap around to 2
                self.cards[mutateIndex][typeOrSuit] = (mutatedCard + amountToMutate) % 13
            else:
                # no negative card numbers allowed, either
                self.cards[mutateIndex][typeOrSuit] = abs(mutatedCard - amountToMutate)
            legal = self.checkLegality(self.cards)

    # calculates a fitness score for the hand, saves it to the fitness variable, and returns the #
    def calculateFitness( self ):
        # since a poker hand's type is the highest possible type it could be
        # we're just going to test for the different kinds of hands starting from the best to the worst

        # sort the cards by card type
        self.cards.sort()

        # ROYAL FLUSH
        # = card type order is 1, 10, 11, 12, 13 and same suit
        count = 0
        prevCardType = self.cards[0][1]
        for cardType, suit in self.cards:
            if cardType == prevCardType:
                count += count
        if (count == 4 and
            self.cards[0][0] == 1 and
            self.cards[1][0] == 10 and
            self.cards[2][0] == 11 and
            self.cards[3][0] == 12 and
            self.cards[4][0] == 13):
            self.fitness = self.fitnessScoreDistribution[0]
            return self.fitnessScoreDistribution[0]

        # FOUR OF A KIND
        # = card type order is the same four times in a row
        prevCardType = self.cards[0][0]
        count = 0
        for cardType, suit in self.cards:
            if cardType == prevCardType:
                count += 1
            else:
                prevCardType = cardType
                count = 0
        if count == 4:
            self.fitness = self.fitnessScoreDistribution[1]
            return self.fitnessScoreDistribution[1]

        # STRAIGHT FLUSH
        # = cards are in numerical order and identical suits
        prevCardType = self.cards[0][0]
        prevSuit = self.cards[0][1]
        count = 0
        for cardType, suit in self.cards:
            if suit == prevSuit and cardType == prevCardType + 1:
                count += 1
                prevCardType = cardType
        if count == 4:
            self.fitness = self.fitnessScoreDistribution[2]
            return self.fitnessScoreDistribution[2]

        # FULL HOUSE
        # = three cards of same rank, two of a different matching rank
        # split up hand into first two cards, last two cards, and middle card
        # return if first two cards match, last two cards match, and middle card matches either
        group1 = self.cards[0:2] # first two cards in hand
        group2 = self.cards[3:5] # last two cards in hand
        middle = self.cards[2] # middle card
        group1type = group1[0][0]
        group2type = group2[0][0]

        if (group1type == group1[1][0] and
            group2type == group2[1][0] and
            (middle[0] == group1type or middle[0] == group2type)):
            self.fitness = self.fitnessScoreDistribution[3]
            return self.fitnessScoreDistribution[3]

        # FLUSH
        # = five cards of the same suit
        cardSuit = self.cards[0][1]
        count = 0
        for cardType, suit in self.cards:
            if suit == cardSuit:
                count += 1
        if count == 5:
            self.fitness = self.fitnessScoreDistribution[4]
            return self.fitnessScoreDistribution[4]

        # STRAIGHT
        # = five cards in a row, not necessarily matching suit
        prevCardType = self.cards[0][0]
        count = 0
        for cardType, suit in self.cards:
            if cardType == prevCardType + 1:
                count += 1
                prevCardType = cardType
        if count == 4:
            self.fitness = self.fitnessScoreDistribution[5]
            return self.fitnessScoreDistribution[5]

        # THREE OF A KIND
        # = 3 cards of the same card type
        prevCardType = self.cards[0][0]
        count = 0
        for cardType, suit in self.cards:
            if cardType == prevCardType:
                count += 1
            elif count < 3:
                count = 1
                prevCardType = cardType
        if count == 3:
            self.fitness = self.fitnessScoreDistribution[6]
            return self.fitnessScoreDistribution[6]

        # TWO PAIR
        # = two pairs of two cards of the same card type
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
            self.fitness = self.fitnessScoreDistribution[7]
            return self.fitnessScoreDistribution[7]

        # PAIR
        # = one pair of two cards of the same card type
        prevCardType = self.cards[0][0]
        count = 0
        for cardType, suit in self.cards:
            if cardType == prevCardType:
                count += 1
            elif cardType != prevCardType and count < 2:
                count = 0
        if count == 2:
            self.fitness = self.fitnessScoreDistribution[8]
            return self.fitnessScoreDistribution[8]

        # if none of these
        self.fitness = self.fitnessScoreDistribution[9]
        return self.fitnessScoreDistribution[9]
