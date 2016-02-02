
class hand :
    # a hand of cards is defined as a list of tuples
    # where the first is the number of the card (1 - 13)
    # and the second is the suit
    def __init__( self, cards ) :
        self.cards = cards

    def __str__( self ) :
       returnString = ""
       for card in self.cards:
           returnString += str(card) + " "
       return returnString
