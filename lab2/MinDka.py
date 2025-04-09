import sys
from collections import defaultdict

states = {}
epsilonClosures = {}

def main():
    lines = [line.rstrip('\n') for line in sys.stdin]

    inputStringsLine = lines[0].split('|')
    inputStrings = [s.split(',') if s else [] for s in inputStringsLine]

    states_line = lines[1].split(',')
    alphabet_line = lines[2].split(',')
    accepting_states_line = lines[3].split(',') 
    startState = lines[4].strip() 
    

    for line in lines[5:]:
        line = line.strip()

        left, right = line.split('->', 1)
        current, symbol = left.split(',', 1)
        symbol = symbol.strip()
        current = current.strip()

        next_states = [s.strip() for s in right.split(',')]
        states[(current,symbol)] = next_states

