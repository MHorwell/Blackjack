class Hand(list):

    def __init__(self, *cards):
        super().__init__([*cards])
        self.total = None
        self.soft = False
        self.__calculate_total()

    def __calculate_total(self):
        total = 0
        ace = False
        self.soft = False
        for card in self:
            if card.value == 1:
                ace = True
            total += card.value
        if ace and total + 10 <= 21:
            self.soft = True
            total += 10
        self.total = total

    def append(self, card):
        super().append(card)
        self.__calculate_total()

    def split(self):
        return Hand(self[0]), Hand(self[1])

    def get_score(self):
        score = self.total
        if score > 21:
            score = 0
        return score

    def __str__(self):
        string = ""
        for index, card in enumerate(self):
            prefix = "a "
            if str(card)[0].lower() in "aeoiu":
                prefix = "an "
            if index + 1 == len(self):
                prefix = " and " + prefix
            elif index != 0:
                prefix = ", " + prefix
            string += prefix + str(card)
        return string
