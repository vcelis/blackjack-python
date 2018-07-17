import unittest
from carddeck.deck import Deck


class DeckTest(unittest.TestCase):
    def test_one(self):
        my_deck = Deck()
        length = len(my_deck)
        string = str(my_deck)
        string_length = len(string)
        self.assertEqual(length, 52)
        self.assertEqual(string_length, 710)


if __name__ == '__main__':
    unittest.main()
