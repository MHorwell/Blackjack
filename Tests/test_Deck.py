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


if __name__ == '__main__':
    unittest.main()
