# -*- coding: utf-8 -*-

from blackjack.game import Game


def draw_table(game):
    print('\n'*100)
    print(f'Current bet: {game.player.bet}\n')
    print('----------PLAYER----------\n')
    print(game.player.hand)
    print('----------DEALER----------\n')
    print(game.dealer.hand)


if __name__ == '__main__':
    game = Game()
    print('Welcome to Blacjack!')
    while True:
        # Create & shuffle the deck, deal two cards to each player
        game.deal()
        # Prompt the Player for their bet
        game.player.setup_bet()
        # Show cards (but keep one dealer card hidden)
        game.player.hand.flip_cards()
        game.dealer.hand.flip_one()
        draw_table(game)
        while True:
            # Prompt for Player to Hit or Stand
            answer = input('HIT or STAND? ').upper()
            if answer not in ['HIT', 'STAND']:
                print('\nOnly HIT or STAND is accepted! Please try again\n')
                continue
            elif answer == 'HIT':
                game.hit()
                draw_table(game)
                continue
            else:  # Answer is STAND
                break
        game.play_dealer()
        draw_table(game)
        game.dealer.hand.flip_one()
        game.dealer.hand.flip_cards()
        draw_table(game)
        winner = game.end_round()
        if winner is True:
            print('Player wins!\n')
        elif winner is None:
            print('Tie!\n')
        else:
            print('Dealer wins!\n')
        # Inform Player of their chips total
        print(f'Balance: ${game.player.balance}\n')
        # Ask to play again
        while True:
            answer = input('Do you want to play again? ').lower()
            if answer not in ['yes', 'no']:
                print('Only Yes or No is accapted! Please try again.\n')
                continue
            else:
                break
        if answer == 'no':
            break
