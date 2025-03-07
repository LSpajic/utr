import sys
from collections import defaultdict

states = {}

def main():
    lines = [line.rstrip('\n') for line in sys.stdin]

    if not lines:
        return

    input_strings_line = lines[0].split('|')
    input_strings = [s.split(',') if s else [] for s in input_strings_line]

    states_line = lines[1].split(',')
    alphabet_line = lines[2].split(',')
    accepting_states_line = lines[3].split(',') 
    start_state = lines[4].strip() 

    transitions = []
    print(lines[5:])

    for line in lines[5:]:
        line = line.strip()

        left, right = line.split('->', 1)
        current, symbol = left.split(',', 1)
        symbol = symbol.strip()
        current = current.strip()

        next_states = [s.strip() for s in right.split(',')]
        transitions.append(((current, symbol), next_states))
        states[(current,symbol)] = next_states

    #for results in states_line:
    #    for transitionVariable in results:
    
    print("--------------------")
    print(input_strings)
    print(states_line)
    print(alphabet_line)
    print(accepting_states_line)
    print(start_state)
    print("Transitions:")
    print(states)


#def getNextStates(current, symbol, transitions):
    

if __name__ == main():
    main()