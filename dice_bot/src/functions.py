"""
===========================================
Author: Codiacs
Github: github.com/MicroOptimization
===========================================
"""
import random

def roll_dice(faces):
    
    return random.randint(1, faces)

def get_sprite_path(face):
    
    return "To be implemented"

def draw_card():
    deck = Deck()
    card = deck.deal()
    
    return card

class Deck:
    
    possible_ranks = ["Two", "Three", "Four", "Five", "Six", 
                           "Seven", "Eight", "Nine", "Ten", "Jack", 
                           "Queen", "King", "Ace"]
    possible_suits = ["Diamonds", "Clubs", "Hearts", "Spades"]
    
    def __init__(self):
        self.cards = []
        
    
    def shuffle(self):
        print("To be implemented")
    
    
    def deal(self):
        rank = self.possible_ranks[random.randint(0, len(self.possible_ranks) - 1)]
        suit = self.possible_suits[random.randint(0, len(self.possible_suits) - 1)]
        
        dealt_card = Card(rank, suit)
        return dealt_card
    
class Card:
    
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        




