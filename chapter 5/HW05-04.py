'''
@author Sai
File name: HW05-04.py
Date created: 7/22/2019
Date last modified: 7/22/2019
Python Version: 3.1
this file creates the deck of cards and shuffles the cards
'''

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return (f"Suit is {self.suit} . Rank is {self.rank}")

def prepare_cards(card_name):
    cards_data = []
    ace = Card(card_name,"ace")
    joker = Card(card_name,"joker")
    king = Card(card_name,"king")
    queen = Card(card_name,"queen")
    for i in range(2,11):
        cards_data.append(Card(card_name,i))
    cards_data.append(ace)
    cards_data.append(joker)
    cards_data.append(king)
    cards_data.append(queen)
    return cards_data



if __name__ == "__main__":
    list_of_cards= ["hearts","diamonds","clubs","spades"]
    total_cards= []

    for card in list_of_cards:
        total_cards.append(prepare_cards(card))

    for each_list in total_cards:
        for each_card in each_list:
            print(each_card)

    random.shuffle(total_cards)    
    print("After shuffling")

    for each_list in total_cards:
        for each_card in each_list:
            print(each_card)
    
    
    


