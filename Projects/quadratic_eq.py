# importing the necessary modules
import math
import itertools

# defining the function to run the quadratic equation on a, b, c
def quadratic(a, b, c):
  # making sure a doesn't equal 0, if it does then you cant solve the quadratic because there would be a DivideByZero Error
  try:
    assert a != 0
  except AssertionError:
    # returns None if a == 0
    return None
  
  # checking to see if there are 0, 1, or 2 solutions to the equation
  discriminant = b**2 - 4 * a * c

  # returns none if there are no real solutions
  if discriminant < 0:
    return None # This equation has no real solution
  # returns the only solution
  elif discriminant == 0:
    x = (-b + math.sqrt(discriminant)) / (2 * a)
    return x # This equation has one solution
  # returns 2 possible solutions to the equation
  else:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return x1, x2 # This equation has 2 solutions

def three_digits():
  # using itertools.product to get every 3 digit combination -> (0, 0, 1), (0, 0, 2) ... (9, 9, 8) (9, 9, 9,)
  p = itertools.product(range(10), repeat=3)
  for num in p:
    yield num # yield the num so it we dont store it all in memory

def test_quadratic():
  nums = three_digits()
  res = [] # storing solutions
  for i in nums: # looping thru the generator
    a, b, c = i # defining a, b, c
    q = quadratic(a, b, c) # running the quadratic equation
    if q is not None: # if the formula doesnt return none
      res.append(q) # add the solution to the list
    else: # if it does return None
      continue # skip o the beginning of the loop
  return res # return the results

if __name__ == '__main__': # <<< standard python syntax
  res = test_quadratic() # testing the quadratic
  print(res) # printing the results
