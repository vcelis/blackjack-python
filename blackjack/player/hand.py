# -*- coding: utf-8 -*-
"""
Module docstring

TODO:
    * Write module docstring
"""


class Hand:
    """Class to represent a hand of playing cards"""

    def __init__(self):
        self.cards = list()
        self.value = 0
        self.aces = 0
        self.bust = False

    def __str__(self):
        result = ''
        for card in self.cards:
            if card.face_up:
                result += f'{str(card)}\n'
            else:
                result += 'HIDDEN CARD\n'
        return result

    def __len__(self):
        return self.value

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.cards):
            result = self.cards[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def add_card(self, card):
        # Add card to self.cards
        self.cards.append(card)
        # Add value of card to self.value
        self.value += card.get_value()
        # Track aces
        if card.get_value() == 11:
            self.aces += 1
        # Adjust value for aces if needed
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 10
        # Check for bust and toggle self.bust
        self.bust = self.value > 21

    def clear(self):
        self.__init__()

    def flip_cards(self):
        for card in self.cards:
            card.flip()

    def flip_one(self):
        try:
            self.cards[0].flip()
        except IndexError:
            pass
