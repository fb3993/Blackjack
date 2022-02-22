#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 10:48:21 2022

@author: filber
"""
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def restart(self):
        self.all_cards =[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
        self.shuffle()

    def deal_one(self):
        return self.all_cards.pop()

class Person:

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def get_curr_cards(self):
        return self.all_cards

    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards/'

class Player(Person):

    def __init__(self,name,amount):
        Person.__init__(self,name)
        self.amount = amount

    def get_curr_amount(self):
        return self.amount

    def change_amount(self,amount):
        self.amount += amount

class Dealer(Person):

    def __init__(self,name):
        Person.__init__(self,name)
