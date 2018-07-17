# -*- coding: utf-8 -*-
"""
Module docstring

TODO:
    * Write module docstring
"""
import random

from .card import Card


class Deck:
    """Class to represent a deck of cards
    """
    def __init__(self):
        self.cards = list()
        self.populate()

    def __str__(self):
        """Returns a string of the cards when casted into a string"""
        result = f'{len(self.cards)} cards in the deck.'
        for card in self.cards:
            result += f'\n{str(card)}'
        return result

    def __len__(self):
        """Returns an integer representing the amount of cards  in deck"""
        return len(self.cards)

    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self.cards)

    def populate(self, shuffle=True):
        """Populates a deck of 52 cards"""
        self.cards.clear()
        for suit in range(len(Card.suit_values)):
            for rank in range(1, len(Card.rank_values)):
                card = Card(Card.rank_values[rank], Card.suit_values[suit])
                self.cards.append(card)
        if shuffle:
            self.shuffle()

    def deal_card(self):
        """Removes and returns card at top of deck.
        If the deck is empty, return None
        """
        try:
            return self.cards.pop(0)
        except IndexError:
            return None
