import sys
from collections import defaultdict

states = {}
epsilonClosures = {}

def main():
    lines = [line.rstrip('\n') for line in sys.stdin]


    states_line = lines[0].split(',')
    alphabet_line = lines[1].split(',')
    accepting_states_line = lines[2].split(',') 
    startState = lines[3].strip() 
    

    for line in lines[4:]:
        line = line.strip()

        left, right = line.split('->', 1)
        current, symbol = left.split(',', 1)
        symbol = symbol.strip()
        current = current.strip()

        next_states = [s.strip() for s in right.split(',')]
        states[(current,symbol)] = set(next_states)

    reachable_states = {startState}
    new_states = {startState}

    while (new_states != set([])):
        temp = set([])
        for state in new_states:
            for transtion in alphabet_line:
                if (state, transtion) in states.keys():
                    temp = temp.union(states[(state, transtion)])
            print(temp)

        new_states = temp - reachable_states
        reachable_states = reachable_states.union(new_states)

    temp = set({})
    for state in new_states:
        for transtion in alphabet_line:
            temp = temp.union(states[(state, transtion)])
    new_states = temp - reachable_states
    reachable_states = reachable_states.union(new_states)
    print("Tu sam")
    print(reachable_states)

if(__name__ == "__main__"):
    main()