import sys
from collections import defaultdict

states = {}

def main():
    lines = [line.rstrip('\n') for line in sys.stdin]

    input_strings_line = lines[0].split('|')
    input_strings = [s.split(',') if s else [] for s in input_strings_line]

    states_line = lines[1].split(',')
    alphabet_line = lines[2].split(',')
    accepting_states_line = lines[3].split(',') 
    start_state = lines[4].strip() 
    

    for line in lines[5:]:
        line = line.strip()

        left, right = line.split('->', 1)
        current, symbol = left.split(',', 1)
        symbol = symbol.strip()
        current = current.strip()

        next_states = [s.strip() for s in right.split(',')]
        states[(current,symbol)] = next_states
    print("--------------------")

    currState = []
    currState.append(start_state)
    tmpState = []
    for transitionVariable in input_strings[3]:
        for state in currState:
            tmpState = tmpState + getNextStates(state, transitionVariable, states)
            if tmpState == ['#']:
                tmpState = []
            currState = tmpState
            tmpState = []
            print(currState)
        
            
    print("--------------------")
    print("--------------------")
    print(input_strings)
    print(states_line)
    print(alphabet_line)
    print(accepting_states_line)
    print(start_state)
    print("Transitions:")
    print(states)
    print("--------------------")
    print(getNextStates('stanje1', 'a', states))

    nextStates = []
    print(states_line)
    print("----------------")
    

    #for results in states_line:
    #    for transitionVariable in results:
    #



def getNextStates(current, symbol, states):# nadodaj rekurziju ovo radi samo za dubinu 1!!!!
    
    if (current, symbol) in states.keys():
        a = states[(current, symbol)]
        try:
            for parts in a:
                if (parts, '$') in states.keys():
                    a = a + states[(parts, '$')] 
        finally:
            return a
    return ['#']

if __name__ == main():
    main()