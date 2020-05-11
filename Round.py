from Deck import Deck


class Round(object):

    def __init__(self, deck, bet=10.0):
        self.deck = deck
        self.bet = [bet]
        self.player_hands = [deck.create_hand()]
        self.current_hand = 0
        self.dealer_hand = deck.create_hand()
        self.round_over = True
        self.start_round()

    def start_round(self):
        if self.dealer_hand.total == 21 and self.get_current_hand().total == 21:
            print("Push!")
        elif self.get_current_hand().total == 21:
            self.bet[0] = self.bet[0] * 1.5
            print("Player has Blackjack!")
        elif self.dealer_hand.total == 21:
            print("Dealer has Blackjack!")
        else:
            self.round_over = False

    def play(self):
        blackjack = True  # If the round is already over, blackjack has occurred
        while not self.round_over:
            blackjack = False
            print("\nDealer has {}".format(self.dealer_hand[0]))
            print("You have {} in your hand. (Total: {})".format(self.get_current_hand(),
                                                                 self.get_current_hand().total))
            option = input("Please select an option: ")
            if option.lower() == "hit":
                self.hit()
            elif option.lower() == "double":
                self.double()
            elif option.lower() == "split":
                valid = self.split()
                if not valid:
                    print("You can't split this hand.")
                else:
                    self.bet.append(self.bet[0])
                    self.draw()
            elif option.lower() == "stay":
                self.finish_hand()
        if not blackjack:
            self.dealer_play()
        return self.calculate_winnings()

    def draw(self):
        card = self.deck.pop(0)
        print("You draw {}".format(card))
        self.get_current_hand().append(card)

    def hit(self):
        self.draw()
        score = self.get_current_hand().get_score()
        if score == 0:
            print("Bust!")
            self.finish_hand()
        elif score == 21:
            self.finish_hand()

    def double(self):
        self.bet[self.current_hand] = self.bet[self.current_hand] * 2
        self.draw()
        self.finish_hand()

    def split(self):
        success = False
        hand_to_split = self.get_current_hand()
        if len(hand_to_split) == 2 and hand_to_split[0].value == hand_to_split[1].value and len(self.player_hands) < 4:
            selected_hand = self.player_hands.pop(self.current_hand)
            self.player_hands.extend(selected_hand.split())
            success = True
        return success

    def finish_hand(self):
        self.round_over = True
        if self.current_hand + 1 < len(self.player_hands):
            self.current_hand += 1
            self.round_over = False
            self.draw()

    def get_current_hand(self):
        return self.player_hands[self.current_hand]

    def dealer_play(self):
        print()
        while self.dealer_hand.total < 17 or (self.dealer_hand.soft and self.dealer_hand.total == 17):
            card = self.deck.pop(0)
            print("Dealer draws {}".format(card))
            self.dealer_hand.append(card)
        print("Dealer has {} (Total: {})".format(self.dealer_hand, self.dealer_hand.total))

    def calculate_winnings(self):
        winnings = 0
        dealer_score = self.dealer_hand.get_score()
        for index, hand in enumerate(self.player_hands):
            if hand.get_score() < dealer_score:
                winnings -= self.bet[index]
            elif hand.get_score() > dealer_score:
                winnings += self.bet[index]
        return winnings


if __name__ == "__main__":
    deck = Deck()
    print(Round(deck).play())
