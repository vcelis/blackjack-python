# -*- coding: utf-8 -*-
"""
Module docstring

TODO:
    * Write module docstring
"""


class Card:
    """Class to represent a playing card of a deck

    Required Attributes:
        Rank: x = Integer 1-13 from Card.rank_values list
            [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack', 'Queen', 'King']
        Suit: x = Integer 0-3 from Card.suit_values list
            ['Hearts', 'Spades', 'Clubs', 'Diamonds']

    Optional Attributes:
        face_up: boolean False by default.
    """
    rank_values = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                   'Jack', 'Queen', 'King']
    suit_values = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

    def __init__(self, rank, suit, face_up=False):
        self.rank = rank
        self.suit = suit
        self.face_up = face_up

    def __str__(self):
        """Returns a string when casted into a string"""
        return f'{self.rank} of {self.suit}'

    def flip(self):
        """Flips the face_up boolean value"""
        self.face_up = not self.face_up

    def get_value(self):
        """Returns an integer coresponding with the card value"""
        value = Card.rank_values.index(self.rank)
        return value if value <= 10 else 10
