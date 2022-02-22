#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 11:11:04 2022

@author: filber
"""
import blackjack_functions as funcs
import blackjack_classes

# variables

player = blackjack_classes.Player(name="One",amount=100)
dealer = blackjack_classes.Dealer(name="Dealer")
deck = blackjack_classes.Deck()

games_won = 0
games_lost = 0
games_draw = 0
games_bj = 0

# Functions

def play_game():

    global games_won
    global games_lost
    global games_draw
    global games_bj

    deck.restart()
    player.all_cards = []
    dealer.all_cards = []

    game_on = True
    bust = False
    result = 0

    # player places initial bet
    bet = funcs.place_bet(player.get_curr_amount())
    player.change_amount(-bet)

    # Deal first round of cards
    player.add_cards(deck.deal_one())
    dealer.add_cards(deck.deal_one())
    player.add_cards(deck.deal_one())
    dealer.add_cards(deck.deal_one())

    player_cards = player.get_curr_cards()
    dealer_cards = dealer.get_curr_cards()
    player_hand = funcs.card_values(player_cards)
    dealer_hand = funcs.card_values(dealer_cards)

    # Display cards
    funcs.display_cards(player_cards,"Player")
    if dealer_hand == 21:
        funcs.display_cards(dealer_cards,"Dealer")
    else:
        print("\nDealer cards:")
        print("\tx")
        print("\t{}".format(dealer_cards[1]))

    # Check for blackjacks
    if player_hand == dealer_hand == 21:
        print("PUSH: both dealer and player have a blackjack. Your bet is returned")
        player.change_amount(bet)
        game_on = False
        games_draw += 1
    elif player_hand == 21:
        print("Blackjack! You win 1.5x of your bet")
        player.change_amount(bet * 2.5)
        games_bj += 1
        games_won += 1
        game_on = False
    elif dealer_hand == 21:
        print("Dealer's Blackjack! You lose this round!")
        games_lost += 1
        game_on = False

    # continues the game if no blackjacks
    if game_on:

        move = funcs.choose_move(player_cards[0].value == player_cards[1].value)

        if move == 'H':                             # Hit

            while game_on:

                player.add_cards(deck.deal_one())
                player_cards = player.get_curr_cards()
                player_hand = funcs.card_values(player_cards)
                funcs.display_cards(player_cards,"Player")

                if player_hand > 21:
                    bust = True
                    game_on = False
                else:
                    continue_hit = input("Do you want another card (H) or do you stand (S)? ").upper()
                    if continue_hit == 'S':
                        game_on = False

        elif move == 'D':                           # Double Down
            # Doubles the bet
            if player.get_curr_amount() > bet:
                player.change_amount(-bet)
                bet *= 2
            else:
                curr_amount = player.get_curr_amount()
                player.change_amount(-curr_amount)
                bet += curr_amount
            player.add_cards(deck.deal_one())
            player_cards = player.get_curr_cards()
            funcs.display_cards(player_cards,"Player")
            player_hand = funcs.card_values(player_cards)
            if player_hand > 21:
                bust = True
                game_on = False
        elif move == 'P':                           # Split

            if player.get_curr_amount() >= bet:
                player.change_amount(-bet)
                bet += 2
            else:
                bet += player.get_curr_amount()
                player.change_amount(-player.get_curr_amount())

            player.add_cards(deck.deal_one())
            player.add_cards(deck.deal_one())
            player_cards = player.get_curr_cards()
            player_hand = funcs.card_values(player_cards,True)
            display_cards(player_cards,"Player")
        elif move == 'U':                           # Surrender
            print("Surrender: you get half of your bet back and forfeit this hand.")
            player.change_amount(bet / 2)
        else:                                       # Stand
            print("Stand: the dealer will get cards.\n")

        if bust:
            print("You lost the game")
            result = 0
            # Forefeit bet
            dealer_play = False
        else:
            print("\nThe dealer will now play.\n")
            dealer_play = True

        while dealer_play:
            dealer_hand = funcs.card_values(dealer_cards)
            if dealer_hand >= 17: dealer_play = False
            else:
                dealer.add_cards(deck.deal_one())
        dealer_cards = dealer.get_curr_cards()
        funcs.display_cards(dealer_cards,"Dealer")

        if dealer_hand > 21:
            print("The dealer went bust. You win.")
            result = 1
        elif game_on:
            result = funcs.check_win(dealer_hand,player_hand)

        if result == 2:
            print("Even")
            player.change_amount(bet)
            games_draw += 1
        if result == 0:
            print("The dealer wins")
            games_lost += 1
        if result == 1:
            print("You win!")
            player.change_amount(bet*2)
            games_won += 1

funcs.instructions(player.get_curr_amount())

while True:

    play_game()
    funcs.display_update(games_won,games_lost,games_draw,games_bj,player.get_curr_amount())

    if player.get_curr_amount() > 0:
        choice = input("Do you want to play again? (Y/N)    ").upper()
        if choice == "Y": pass
        else:
            print("Thank you for playing.\nFinal results: ")
            funcs.display_update(games_won,games_lost,games_draw,games_bj,player.get_curr_amount())
            break
    else:
        print("You have no money left. You are out of this game.\nFinal results:")
        funcs.display_update(games_won,games_lost,games_draw,games_bj,player.get_curr_amount())
        break
