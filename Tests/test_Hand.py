import unittest
from unittest.mock import Mock

from Hand import Hand


class HandTest(unittest.TestCase):

    def test_hand_initialise_one_card(self):
        mock_card = Mock()
        mock_card.value = 2
        self.assertEqual(Hand(mock_card).total, 2)

    def test_hand_initialise_two_cards(self):
        mock_card_one, mock_card_two = Mock(), Mock()
        mock_card_one.value = 2
        mock_card_two.value = 4
        self.assertEqual(Hand(mock_card_one, mock_card_two).total, 6)

    def test_add_to_hand(self):
        mock_card_one, mock_card_two = Mock(), Mock()
        mock_card_one.value = 3
        mock_card_two.value = 7
        test_hand = Hand(mock_card_one)
        test_hand.append(mock_card_two)
        self.assertEqual(test_hand.total, 10)

    def test_ace_in_hand(self):
        mock_card = Mock()
        mock_card.value = 1
        self.assertEqual(Hand(mock_card).total, 11)

    def test_two_aces_in_hand(self):
        mock_card_one, mock_card_two = Mock(), Mock()
        mock_card_one.value = 1
        mock_card_two.value = 1
        test_hand = Hand(mock_card_one)
        test_hand.append(mock_card_two)
        self.assertEqual(test_hand.total, 12)

    def test_ace_in_hand_over(self):
        mock_card_one, mock_card_two = Mock(), Mock()
        mock_card_one.value = 1
        mock_card_two.value = 12
        test_hand = Hand(mock_card_one)
        test_hand.append(mock_card_two)
        self.assertEqual(test_hand.total, 13)

    def test_hand_split(self):
        mock_card_one, mock_card_two = Mock(), Mock()
        mock_card_one.value = 4
        mock_card_two.value = 5
        test_hand_one, test_hand_two = Hand(mock_card_one, mock_card_two).split()
        self.assertEqual(test_hand_one.total, 4)
        self.assertEqual(test_hand_two.total, 5)


if __name__ == '__main__':
    unittest.main()
