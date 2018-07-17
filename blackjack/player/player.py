# -*- coding: utf-8 -*-
"""
Module docstring

TODO:
    * Write module docstring
"""
from .playerbase import PlayerBase


class Player(PlayerBase):
    """Class to represent the human player
    """
    def __init__(self, balance=1000, bet=10):
        super().__init__()
        self.balance = balance
        self.bet = bet

    def __str__(self):
        result = f'Balance: ${self.balance}'
        result += f'\nBet: ${self.bet}'
        for card in self.hand:
            result += f'\n{str(card)}'
        return result

    def setup_bet(self):
        while True:
            try:
                answer = int(input('How much would you like to bet? '))
                if answer not in range(1, self.balance + 1):
                    print('Invalid bet! Try again.')
                    continue
            except ValueError:
                print('Only an integer is allowed!')
                continue
            else:
                self.bet = answer
                # Deduct bet from balance. Should be in game.end_round()
                self.balance -= self.bet
                break
