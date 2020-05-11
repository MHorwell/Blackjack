import unittest
from unittest.mock import Mock

from Card import Card


class CardTest(unittest.TestCase):

    def test_value_over_calculation(self):
        mock_rank = Mock()
        mock_rank.value = 13
        self.assertEqual(Card(None, mock_rank).value, 10)

    def test_value_under_calculation(self):
        mock_rank = Mock()
        mock_rank.value = 9
        self.assertEqual(Card(None, mock_rank).value, 9)

    def test_face_card_false(self):
        mock_rank = Mock()
        mock_rank.value = 10
        self.assertFalse(Card(None, mock_rank).face_card)

    def test_face_card_true(self):
        mock_rank = Mock()
        mock_rank.value = 11
        self.assertTrue(Card(None, mock_rank).face_card)

    def test_to_string(self):
        mock_rank, mock_suit = Mock(), Mock()
        mock_rank.name = "Testrank"
        mock_rank.value = 0
        mock_suit.value = "TestSuit"
        self.assertEqual(str(Card(mock_suit, mock_rank)), "Testrank of TestSuit")


if __name__ == '__main__':
    unittest.main()
