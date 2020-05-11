import unittest
from unittest.mock import patch

from Deck import Deck


class DeckTest(unittest.TestCase):

    def test_deck_size(self):
        self.assertEqual(len(Deck()), 52)

    def test_deck_unique(self):
        existing_combinations = []
        for card in Deck():
            self.assertFalse(str(card) in existing_combinations)
            existing_combinations.append(str(card))

    @patch("Deck.shuffle")
    def test_deck_shuffled_on_init(self, mock_shuffle):
        deck = Deck()
        mock_shuffle.assert_called_once_with(deck)

    @patch("Deck.Hand")
    def test_create_hand(self, mock_hand):
        test_deck = Deck()
        first_two_cards = test_deck[:2]
        test_deck.create_hand()
        mock_hand.assert_called_once_with(first_two_cards)
        self.assertEqual(len(test_deck), 50)


if __name__ == '__main__':
    unittest.main()
