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
      if self.is_empty():
         return '$'
      if self.stack == '$':
         return '$'
      else:
         return self.stack
   
   def add(self, item):
      self.pop()
      if item != '$':
         self.push(item)
      return self.top()

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

   #print('Ulazni nizovi: ', inputStringsLine)
   #print('Stanja: ',states_line)
   #print('Alfabet: ',alphabet_line)
   #print('Stog Alfabet:',stog_alphabet_line)
   #print('Prihvatljiva stanja: ',accepting_states_line)
   #print('Pocetno stanje: ',startState)
   #print('Pocetno stanje stoga: ',startStogState)
   #PrintDict()
   #
   #print('_______________________________________')

   for inputString in inputStrings:
      flag = 0
      nextState = None
      stack = Stack()
      stack.push(startStogState)
      currentState = startState
      inputString.append('$') 
      print(currentState + '#' + str(stack) + '|' , end='')
      inputCharN = 0
      while inputCharN < len(inputString):
         inputChar = inputString[inputCharN]
         nextState = states.get((currentState, inputChar, stack.top()))
         if inputChar == '$':
            endReached = True
         if nextState is None:
            inputCharN -= 1
            nextState = states.get((currentState, '$', stack.top()))
            if nextState is None:
               if inputChar == '$':
                  if (currentState in accepting_states_line) and endReached:
                     print("1")
                  else:
                     print("0")
               else:
                  print("fail|0")
               flag = 1

               break
         stack.add(nextState[1])
         currentState = nextState[0]
         print(currentState + '#' + str(stack) + '|' , end='')
         inputCharN += 1

      if flag == 0:
         if (currentState in accepting_states_line) and endReached:
            print("1")
         else:
            print("0")


if __name__ == "__main__":
   main()