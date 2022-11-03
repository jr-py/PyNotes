""" The first dunder method we will be talking about is the __init__ method, it
is called whenever an new instance of a class is made. Ex: """

class Obj1:
  def __init__(self, t):
    self.type = t
    print(f"Type {self.type} has been made!")
 
new_obj1 = Obj1(3) # will print: Type 3 has been made!

# --------------------------------------------------------------------------------------------------------------------------------------------------------------

""" The next dunder method is __repr__. It is called whenever you try to print an object """

class Obj2:
  def __init__(self, t):
    self.type = t
  
  def __repr__(self):
    return f"Obj2(self.type)" # this is the typical format you use
    
new_obj2 = Obj2(3) # will print: Type 3 has been made!
print(new_obj2) # will print: Obj2(3)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------

""" For the following methods, I am going to combine them since they are more or less the same
(__lt__ -> obj < x), (__le__ -> obj <= x), (__eq__ -> obj == x), (__ne__ -> obj != x), (__gt__ -> obj > x), (__ge__ -> obj >= x) 
Here is an example: """

class Obj3:
  def __init__(self, t, v):
    self.type = t
    self.value = v
    
  """ We use if isinstance to make sure the other object is of the same class"""
  # less then
  def __lt__(self, other):
    if isinstance(other, Obj3):
      return self.v < other.v
    return False
  
  # less then or equal to
  def __le__(self, other):
    if isinstance(other, Obj3):
      return self.v <= other.v
    return False
  
  # equal to
  def __eq__(self, other):
    if isinstance(other, Obj3):
      return self.v == other.v
    return False
  
  # not equal to
  def __ne__(self, other):
    if isinstance(other, Obj3):
      return self.v != other.v
    return False
  
  # greater than 
  def __gt__(self, other):
    if isinstance(other, Obj3):
      return self.v > other.v
    return False
  
  # greater than or equal to
  def __ge__(self, other):
    if isinstance(other, Obj3):
      return self.v >= other.v
    return False
  
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
  
