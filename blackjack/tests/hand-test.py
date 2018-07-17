import unittest
from player.hand import Hand
from carddeck.card import Card


class HandTest(unittest.TestCase):
    def test_one(self):
        my_hand = Hand()
        my_hand.add_card(Card(Card.rank_values[1], Card.suit_values[1]))
        my_hand.add_card(Card(Card.rank_values[5], Card.suit_values[3]))
        my_hand.add_card(Card(Card.rank_values[5], Card.suit_values[2]))
        self.assertEqual(my_hand.value, 11)
        self.assertEqual(my_hand.soft_value, 21)
        self.assertEqual(len(my_hand), 11)
        expected = 'Ace of Spades\n5 of Diamonds\n5 of Clubs\n'
        self.assertEqual(str(my_hand), expected)
        self.assertEqual(my_hand.dealer, False)
        self.assertEqual(my_hand.blackjack, True)


if __name__ == '__main__':
    unittest.main()
