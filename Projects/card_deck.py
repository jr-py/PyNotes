# importing modules
import random # .shuffle

# creating the class
class Deck:
  # using the __init__ constructor
  def __init__(self):
    # the 4 suits in a deck
    self.suits = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
    # the 13 types of cards
    self.cards = ('King', 'Queen', 'Jack', 'Ace', '10', '9', '8', '7', '6', '5', '4', '3', '2')
    # creating the deck
    self.deck = [(i, j) for i in self.cards for j in self.suits]
    self.reset() # standard py syntax

  def __repr__(self):
    # how to represent the deck
    return '\n'.join(f"{x[0]} of {x[1]}" for x in self.deck)
  
  def reset(self):
    # just reseting the deck
    self.deck = [(i, j) for i in self.cards for j in self.suits]

  def shuffle(self):
    # shuffling the deck
    random.shuffle(self.deck)

  def remove_card(self):
    # havent gotten to this part
    pass
      
  def pick_card(self):
    # picking random card in the deck
    card = random.choice(self.deck)
    return f"{card[0]} of {card[1]}"

# testing out the deck
d = Deck()
c = d.pick_card()
d.shuffle()
print(d)
d.reset()
print(d)
