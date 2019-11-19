# https://codereview.stackexchange.com/questions/196528/simple-python-dice
import random

class Dice:
    def __init__(self, sides):
        self._len = sides

    def __len__(self):
        return self._len

    def __getitem__(self, x):
        return x + 1

def game():
   d = Dice(6)
   dice = random.choice(d)

   if dice in (2,3,12):
      return False

   if dice in (7,11):
      return True

   # keep rolling
   while True:
      new_roll = random.choice(d)

      # re-rolled the initial value => win
      if new_roll==dice:
         return True

      # rolled a 7 => loss
      if new_roll == 7:
         return False

      # neither won or lost, the while loop continues ..
        
#d = Dice(6)
#print( random.choice(d) )
#print( random.choices(d, k=10) )
print( game() )