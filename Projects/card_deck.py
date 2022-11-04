import random

class Deck:
  def __init__(self):
    self.suits = ('Clubs', 'Spades', 'Hearts', 'Diamonds')
    self.cards = ('King', 'Queen', 'Jack', 'Ace', '10', '9', '8', '7', '6', '5', '4', '3', '2')
    self.deck = [(i, j) for i in self.cards for j in self.suits]
    self.reset()

  def __repr__(self):
    return '\n'.join(f"{x[0]} of {x[1]}" for x in self.deck)
  
  def reset(self):
    self.deck = [(i, j) for i in self.cards for j in self.suits]

  def shuffle(self):
    random.shuffle(self.deck)

  def remove_card(self):
    pass
      
  def pick_card(self):
    card = random.choice(self.deck)
    return f"{card[0]} of {card[1]}"

d = Deck()
c = d.pick_card()
d.shuffle()
print(d)
