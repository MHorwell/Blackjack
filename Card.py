class Card(object):

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value, self.face_card = self.__calculate_value()

    def __calculate_value(self):
        """
        Checks if card is face card if it is, sets value to 10.
        :return: tuple containing value as int and bool for face_card
        """
        value = self.rank.value
        face_card = False
        if value > 10:
            value = 10
            face_card = True
        return value, face_card

    def __str__(self):
        return "{} of {}".format(self.rank.name, self.suit.value)
