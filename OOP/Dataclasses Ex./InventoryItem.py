from dataclasses import dataclass

@dataclass
class InventoryItem:
  """Class for keeping track of an item in inventory."""
  name: str
  unit_price: float
  quantity_on_hand: int = 0

  def total_cost(self) -> float:
    return self.unit_price * self.quantity_on_hand
    
  def remove_item(self, r):
    if r >= self.quantity_on_hand:
      self.quantity_on_hand = 0
    else:
      if self.quantity_on_hand == 1 or self.quantity_on_hand == 0:
        self.quantity_on_hand = 0
      else:
        self.quantity_on_hand -= r
  
class Store:
  """Container for storing item count & cost"""
  def __init__(self, inventory):
    self.inventory = inventory # going to be a list of InventoryItem objects

  def __repr__(self):
    if len(self.inventory) == 0:
      return "This store has no items"
    else:
      return "\n".join([str(item) for item in self.inventory])

  def __eq__(self, other):
    return self.value() == other.value()
  
  def value(self):
    return sum([item.total_cost() for item in self.inventory])

  def add_item(self, item):
    self.inventory.append(item)

  def restock_specific_item(self, item, amnt):
      """Doesn't do anything if item doesnt exist"""
      for obj in self.inventory:
        if obj.name == item:
          obj.quantity_on_hand += amnt
        else:
          continue
  
  def restock_all_items(self, amnt):
    """Restocks all items in the store"""
    for obj in self.inventory:
      obj.quantity_on_hand += amnt
     
