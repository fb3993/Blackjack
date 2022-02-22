#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 15:27:29 2022

@author: filber
"""

def instructions(starting_amount):
    print("\nWelcome to Blackjack 1.0.\n")
    print("You will play a standard game of blackjack. You start with {}€ and you can continue playing as long as you have money, or you can quit earlier.".format(starting_amount))
    print("The choices you have available are:\n\tSTAND (S): You are happy with your hand and will let the dealer play.\n\tHIT (H): you can ask for additional cards, as long as you don't go bust.\n\tDOUBLE DOWN (D): You double your current bet and ask for one additional card.\n\tSPLIT (P): You split your current hand and double your wager. You are then delt a second card for each of your original cards that play as separate hands.\n\tSURRENDER (U): You surrender your hand, getting back half of your original bet.\n")

def place_bet(curr_amount):

    bet_missing = True
    amount = 0

    while bet_missing:
        try:
            amount = int(input("Place a bet: "))
        except:
            pass

        if curr_amount >= amount and amount > 0:
            print("Bet placed. Current money: {}€".format(curr_amount-amount))
            bet_missing = False
        else:
            print("Invalid amount, please place another bet.")

    return amount

def card_values(cards, split=False):

    total = 0
    ace = 0

    if split:
        total = max(cards[0].value + cards[2].value,cards[1].value + cards[3].value)

    else:
        for card in cards:
            total += card.value
            if card.rank == 'Ace': ace += 1

        for i in range(ace):
            if total > 21:
                total -= 10

    return total

def choose_move(split=False):
    choice = ''

    while True:
        choice = input("\nEnter your move (S/H/D/P/U): ").upper()

        if choice == 'S' or choice == 'H' or choice == 'D' or choice == 'P' or choice == 'U':
            if choice == 'P' and not split: print("You cannot split, your cards are of different value. Please make another choice")
            else: break
        else: print("Invalid choice, please make another one.")

    return choice

def display_cards(cards,role):
    print("\n{} cards:".format(role))
    for card in cards:
        print("\t{}".format(card))

def check_win(dealer, player):

    if dealer == player:
        return 2
    elif dealer > player:
        return 0
    else:
        return 1

def display_update(won,lost,draw,bj,curr_amount):
    print("\n\nWon\tLost\tDraw\tBlack Jacks\n{}\t{}\t{}\t{}\n".format(won,lost,draw,bj))
    print("You have {}€ left.".format(curr_amount))
