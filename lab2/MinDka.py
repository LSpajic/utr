import sys
from collections import defaultdict

states = {}

def main():
    lines = [line.rstrip('\n') for line in sys.stdin]


    states_line = lines[0].split(',')
    SetStates = set(states_line)

    alphabet_line = lines[1].split(',')
    alphabet = set(alphabet_line)

    accepting_states_line = lines[2].split(',') 
    accepting_states = set(accepting_states_line)

    not_accepting_states = SetStates - accepting_states

    startState = lines[3].strip() 
    

    for line in lines[4:]:
        line = line.strip()

        left, right = line.split('->', 1)
        current, symbol = left.split(',', 1)
        symbol = symbol.strip()
        current = current.strip()
        states[(current,symbol)] = right
    #print(states)

    reachable_states = {startState}
    new_states = {startState}

    
    while (new_states != set([])):
        temp = set([])
        for state in new_states:
            for transtion in alphabet_line:
                if (state, transtion) in states.keys():
                    temp.add(states[(state, transtion)])
            #print(temp)

        new_states = temp - reachable_states
        reachable_states = reachable_states.union(new_states)

    temp = set({})
    for state in new_states:
        for transtion in alphabet_line:
            temp = temp.union(states[(state, transtion)])
    new_states = temp - reachable_states
    reachable_states = reachable_states.union(new_states)
    #print("Tu sam")
    accepting_states = accepting_states.intersection(reachable_states)
    not_accepting_states = not_accepting_states.intersection(reachable_states)
    statesgroups = [accepting_states, not_accepting_states]

    states2 = {}

    for state in reachable_states:
        for transtion in alphabet_line:
            if (state, transtion) in states.keys():
                if states[(state, transtion)] not in accepting_states:
                    states2[(state, transtion)] = None
                else:
                    states2[(state, transtion)] = states[(state, transtion)]
            
            else:
                states2[(state, transtion)] = None
    
    #metoda tablice
    #prvo ziceri (dva stanja ne mogu bit istovjetni ako su razliciti po prihvatljivosti)
    temp = set([])
    for group in statesgroups:
        for first in range(0, len(group)):
            for second in range(i+1, len(group)):
                pass  

    


if(__name__ == "__main__"):
    main()