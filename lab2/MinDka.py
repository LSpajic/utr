import sys
from collections import defaultdict

states = {}
AllTranstions = {}
alphabet_line = []
isAccepting = {}

def getGroups(group1, group2, accepting_states, not_accepting_states):
    temp = set([])

def returnGroups(state1, groups):
    a = []
    for state in AllTranstions[state1]:
        for i in range(0, len(groups)):
            if state in groups[i]:
                a.append(i)

    return a

def isNotSame(state1, state2, groups):
    print("state1", state1)
    print("state2", state2)
    print("groups", groups)
    print("AllTranstions[state1]", AllTranstions[state1])
    print("AllTranstions[state2]", AllTranstions[state2])

    a1 = []
    a2 = []
    a1 = returnGroups(state1, groups)
    a2 = returnGroups(state2, groups)
    if a1 != a2:
        return True
    return False
def main():
    lines = [line.rstrip('\n') for line in sys.stdin]


    states_line = lines[0].split(',')
    SetStates = set(states_line)

    alphabet_line = lines[1].split(',')

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
        AllTranstions[state] = []
        for transtion in alphabet_line:
            AllTranstions[state].append(states[(state, transtion)])
    print(AllTranstions)
            #print("-------")
    print("accepting states")    
    for state in accepting_states:
        print(state, "->", AllTranstions[state])
    print("not accepting states")    
    for state in not_accepting_states:
        print(state, "->", AllTranstions[state])
    listaaa = []
    temp = []
    acs = list(accepting_states)
    print(acs)
    print("accepting states", accepting_states)
    print("not accepting states", not_accepting_states)
    for i in range(0, len(accepting_states)):
        for j in range(i+1, len(accepting_states)):
            if not isNotSame(acs[i], acs[j], [accepting_states, not_accepting_states]):
                print(acs[i], acs[j])
                temp.append(acs[i])
                temp.append(acs[j])
                listaaa.append(temp)
                temp = []

    ncs = list(not_accepting_states)
    for i in range(0, len(not_accepting_states)):
        for j in range(i+1, len(not_accepting_states)):
            if not isNotSame(ncs[i], ncs[j], [accepting_states, not_accepting_states]):
                print("ncs:",ncs[i], ncs[j])
                temp.append(ncs[i])
                temp.append(ncs[j])
                listaaa.append(temp)
                temp = []
    print("LISTA")
    print(listaaa)

    #metoda tablice
    #prvo zic3eri (dva stanja ne mogu bit istovjetni ako su razliciti po prihvatljivosti)


    


if(__name__ == "__main__"):
    main()