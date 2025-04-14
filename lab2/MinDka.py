import sys
from collections import defaultdict

states = {}
AllTranstions = {}
alphabet_line = []
isAccepting = {}
    
#def getGroups(group1, group2, accepting_states, not_accepting_states):
#    temp = set([])

def formatOutput1(states):
    return ','.join(states)
def returnGroups(state1, groups):
    a = []
    #print("state1", AllTranstions[state1]) 

    for state in AllTranstions[state1]:
        #print("state1", state1)
        for i in range(0, len(groups)):
            if state in groups[i]:
                a.append(i)
    a = tuple(a)
    return a

#def isNotSame(state1, state2, groups):
#    print("state1", state1)
#    print("state2", state2)
#    print("groups", groups)
#    print("AllTranstions[state1]", AllTranstions[state1])
#    print("AllTranstions[state2]", AllTranstions[state2])
#
#    a1 = []
#    a2 = []
#    a1 = returnGroups(state1, groups)
#    a2 = returnGroups(state2, groups)
#    if a1 != a2:
#        return True
#    return False
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
            temp = temp.uniontranstions(states[(state, transtion)])
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
        #print("AllTranstions[state]", AllTranstions[state])
    #print("-------")
    #print("accepting states")    
    #for state in accepting_states:
    #    print(state, "->", AllTranstions[state])
    #print("not accepting states")    
    #for state in not_accepting_states:
    #    print(state, "->", AllTranstions[state])
    #listaaa = []
    #temp = []
    #acs = list(accepting_states)
    ##print(acs)
    #print("accepting states", accepting_states)
    #print("not accepting states", not_accepting_states)
    #for i in range(0, len(accepting_states)):
    #    for j in range(i+1, len(accepting_states)):
    #        if not isNotSame(acs[i], acs[j], [accepting_states, not_accepting_states]):
    #            #print(acs[i], acs[j])
    #            temp.append(acs[i])
    #            temp.append(acs[j])
    #            acs.remove(acs[j])
    #            listaaa.append(temp)
    #            temp = []
#
    #            
#
    #ncs = list(not_accepting_states)
    #for i in range(0, len(not_accepting_states)):
    #    for j in range(i+1, len(not_accepting_states)):
    #        if not isNotSame(ncs[i], ncs[j], [accepting_states, not_accepting_states]):
    #            #print("ncs:",ncs[i], ncs[j])
    #            temp.append(ncs[i])
    #            temp.append(ncs[j])
    #            listaaa.append(temp)
    #            temp = []
    #print("LISTA")
    #print(listaaa)
    accepting_states = list(accepting_states)
    not_accepting_states = list(not_accepting_states)

    #a = returnGroups('p4',[accepting_states, not_accepting_states])
    #print("Grupe",a)

    newDict = {}

    groups = [accepting_states, not_accepting_states]
    while True:
        newGroup = []
        for group in groups:
            tempArr = {}
            for state in group:
                #print("state", state)
                Kojim_grupama_pripada = returnGroups(state, groups)
                if Kojim_grupama_pripada not in tempArr:
                    tempArr[Kojim_grupama_pripada] = set([])
                tempArr[Kojim_grupama_pripada].add(state)
            newGroup.extend(tempArr.values())
            a = list(tempArr.values())
            a.sort()
            #print("tempArr")
            for x in a:
                x = list(x)
                x.sort()
                for i in x:
                    newDict[i] = x[0]

        if newGroup == groups:
            break
        groups = newGroup
            
    #print("Grupe")
    #print(groups)
        
    new_states = []

    new_ac_states = []
    new_nc_states = []

    for sameSteates in groups:
        sameSteates = sorted(sameSteates)
        #print("Grupe", sameSteates)
        if(sameSteates[0] in accepting_states):
            new_ac_states.append(sameSteates[0])
        else:
            new_nc_states.append(sameSteates[0])
        new_states.append(sameSteates[0])

    new_states = sorted(new_states)
    new_ac_states = sorted(new_ac_states)


    print(formatOutput1(new_states))
    print(formatOutput1(alphabet_line))
    print(formatOutput1(new_ac_states))
    print(newDict[startState])
    for state in new_states:
        i = 0
        for transtion in alphabet_line:
            print(state + "," + transtion + "->" + newDict[AllTranstions[state][i]])
            i = i + 1
    #print("novi stanja")
    #print(new_states)
    #print("novi prihvatljivi")
    #print(new_ac_states)
    #print("novi neprihvatljivi")
    #print(new_nc_states)

    


    #metoda tablice
    #prvo zic3eri (dva stanja ne mogu bit istovjetni ako su razliciti po prihvatljivosti)




    


if(__name__ == "__main__"):
    main()
