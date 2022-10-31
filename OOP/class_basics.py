# For definitions of terms see oop-terms.txt
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# To define a class, you use the class keyword followed by the class name. For example, the following defines a Dog class:
class Dog:
  pass

# to create an instance of a class, you put the class name of the class followed by parenthases:
dog = Dog()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
To create attributes for a class the best way is to use the __init__ method
Below is an example of a Cat class with the attributes name and age:
"""

class Cat:
  def __init__(self, name, age):
    self.name = name
    self.age = age

cat = Cat("Buko", 32)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
To create a method, you create a normal function inside as shown above
Below is an example of the fish class with the method feed and how to use it.
"""

class Fish:
  def __init__(self, name, age):
    self.name = name
    self.age = age

   # create a function how you normally would
   def feed(self): # <--- always put self (except for one case)
    """People normally put what a function does right here"""
    print(f"You fed {self.name}") 
    
fish = Fish("Frank", 3)
fish.feed() # runs the function and prints: You fed Frank
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

"""
