# -*- coding: utf-8 -*-
"""
Module docstring

TODO:
    * Write module docstring
"""
from .player.dealer import Dealer
from .player.player import Player
from .carddeck.deck import Deck


class Game():
    """Class to represent the blackjack Game"""

    def __init__(self):
        self.dealer = Dealer()
        self.player = Player()
        self.deck = Deck()

    def __str__(self):
        result = ''
        result += f'Dealer:\n{str(self.dealer)}\n\n'
        result += f'Player:\n{str(self.player)}\n\n'
        result += f'Deck:\n{str(self.deck)}'
        return result

    def deal(self):
        # clear both dealer and player`s hand
        self.dealer.hand.clear()
        self.player.hand.clear()
        # Populate and shuffle deck
        self.deck.populate()
        # Deal 2 cards to the dealer.
        self.dealer.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())
        # Deal 2 cards to the player.
        self.player.hand.add_card(self.deck.deal_card())
        self.player.hand.add_card(self.deck.deal_card())

    def hit(self):
        card = self.deck.deal_card()
        card.flip()
        self.player.hand.add_card(card)

    def stand(self):
        # Return value if <= 21 else return None
        return self.player.hand.value if self.player.hand.value <= 21 else None

    def play_dealer(self):
        # Flip dealers cards over
        # self.dealer.hand.cards[1].flip()
        # Dealer will always hit untill value meets or exceeds 17
        while self.dealer.hand.value < 17:
            self.dealer.hand.add_card(self.deck.deal_card())

    def end_round(self):
        '''Returns True player won, return False dealer wins, None TIE'''
        if not self.player.hand.bust:
            # Player is not bust
            if self.dealer.hand.bust or \
                            self.player.hand.value > self.dealer.hand.value:
                # Dealer is bust or player`s hand is greater
                self.player.balance += self.player.bet * 2
                return True
            elif self.player.hand.value == self.dealer.hand.value:
                # Tie
                self.player.balance += self.player.bet
                return None
        return False
