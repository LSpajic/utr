import sys
from collections import defaultdict
from tabulate import tabulate

states = {}

class Stack:
   def __init__(self):
      self.stack = ""

   def push(self, item):
      self.stack = item + self.stack

   def pop(self):
      if self.stack:
         item = self.stack[0]
         self.stack = self.stack[1:]
         return item
      return None
   def top(self):
      if self.stack:
         return self.stack[0]
      return None
   def is_empty(self):
      return len(self.stack) == 0
   
   def __str__(self):
      return self.stack
   
def PrintDict():
   headers = ["(State, Symbol, Stack)", "(NextState, NextStack)"]
   rows = [ [str(k), str(v)] for k, v in states.items() ]
   print(tabulate(rows, headers=headers, tablefmt="grid"))

def main():
   lines = [line.rstrip('\n') for line in sys.stdin]

   inputStringsLine = lines[0].split('|')
   inputStrings = [s.split(',') if s else [] for s in inputStringsLine]

   states_line = lines[1].split(',')
   alphabet_line = lines[2].split(',')
   stog_alphabet_line = lines[3].split(',')

   accepting_states_line = lines[4].split(',') 
   startState = lines[5].strip() 
   startStogState = lines[6].strip()

   for line in lines[7:]:
      line = line.strip()
      left, right = line.split('->', 1)
      currentState, symbol, currentStog = left.split(',',2)
      NextState, NextStog = right.split(',',1)
      states[(currentState, symbol, currentStog)] = (NextState,NextStog)

   print('Stanja: ',states_line)
   print('Alfabet: ',alphabet_line)
   print('Stog Alfabet:',stog_alphabet_line)
   print('Prihvatljiva stanja: ',accepting_states_line)
   print('Pocetno stanje: ',startState)
   print('Pocetno stanje stoga: ',startStogState)
   PrintDict()
      


if __name__ == "__main__":
   main()