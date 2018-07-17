import unittest
from carddeck.card import Card


class CardTest(unittest.TestCase):
    def test_one(self):
        my_card = Card(Card.rank_values[1], Card.suit_values[0])
        rank = my_card.rank
        suit = my_card.suit
        face_up = my_card.face_up
        value = my_card.get_value()
        self.assertEqual(rank, 'Ace')
        self.assertEqual(suit, 'Hearts')
        self.assertEqual(face_up, False)
        self.assertEqual(value, 1)

    def test_two(self):
        my_card = Card(Card.rank_values[13], Card.suit_values[3])
        rank = my_card.rank
        suit = my_card.suit
        my_card.flip()
        face_up = my_card.face_up
        value = my_card.get_value()
        self.assertEqual(rank, 'King')
        self.assertEqual(suit, 'Diamonds')
        self.assertEqual(face_up, True)
        self.assertEqual(value, 10)

    def test_three(self):
        my_card = Card(Card.rank_values[11], Card.suit_values[2])
        rank = my_card.rank
        suit = my_card.suit
        my_card.flip()
        my_card.flip()
        face_up = my_card.face_up
        value = my_card.get_value()
        self.assertEqual(rank, 'Jack')
        self.assertEqual(suit, 'Clubs')
        self.assertEqual(face_up, False)
        self.assertEqual(value, 10)

    def test_four(self):
        my_card = Card(Card.rank_values[12], Card.suit_values[1])
        rank = my_card.rank
        suit = my_card.suit
        my_card.flip()
        face_up = my_card.face_up
        value = my_card.get_value()
        self.assertEqual(rank, 'Queen')
        self.assertEqual(suit, 'Spades')
        self.assertEqual(face_up, True)
        self.assertEqual(value, 10)


if __name__ == '__main__':
    unittest.main()
