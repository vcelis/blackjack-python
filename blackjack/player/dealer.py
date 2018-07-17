# -*- coding: utf-8 -*-
"""
Module docstring

TODO:
    * Write module docstring
"""
from .playerbase import PlayerBase


class Dealer(PlayerBase):
    """Class to represent the blackjack Dealer
    """
    def __init__(self):
        super().__init__()

    def __str__(self):
        result = ''
        for card in self.hand:
            result += f'\n{str(card)}'
        return result
