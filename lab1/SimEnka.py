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
        if next_states != ['#']:
            states[(current,symbol)] = next_states


    #calculate Epsilon Closure for each state and put it in a dict
    for state in states_line:
        epsilonClosures[state] = genEpsilonClosure(state)
    
    
    #
    # Uzet input
    # krece parsiranje
    #
    #print("--------------------")
    for input_string in inputStrings:
        currState = []
        currState += getEpsilonClosure(startState)
        tmpState = []
        output = []
        output.append(formatOutput(currState))
        #print(formatOutput(currState), end='')
        for transVariable in input_string:
            #print(transVariable)
            for state in currState:
                #tmpState += getNextStates(state, transVariable, states)
                Nstates = getNextStates(state, transVariable)
                for nst in Nstates:
                    if nst not in tmpState:
                        tmpState.append(nst)
            currState = tmpState
            tmpState = []
            if currState == []:
                currState = ['#']
            #currState = list(set(currState))
            currState.sort()

            output.append(formatOutput(currState))
                #print(formatOutput(currState), end='')
        print(formatFinalOutput(output))

        
            
    #print("--------------------")
    #print("--------------------")
    #print(input_strings)
    #print(states_line)
    #print(alphabet_line)
    #print(accepting_states_line)
    #print(start_state)
    #print("Transitions:")
    #print(states)
    #print("--------------------")
    #print(getNextStates('stanje1', 'a', states))

    #nextStates = []
    #print(states_line)
    #print("----------------")
    

    #for results in states_line:
    #    for transitionVariable in results:
    #)
    #print(getNextStates('stanje1', 'a', states))
        
def getEpsilonClosure(current):
    if current in epsilonClosures:
        return epsilonClosures[current]
    else:
        return []


def genEpsilonClosure(current):
    epsilonClosure = [current]
    tmpState = []
    for state in epsilonClosure:
        if (state, '$') in states:
            tmpState = states[(state, '$')]
            #if tmpState not in epsilonClosure:
            #    epsilonClosure.append(tmpState)
            for newState in tmpState:
                if newState not in epsilonClosure:
                    epsilonClosure.append(newState)
    epsilonClosure.sort()
    return epsilonClosure
    
def getNextStates(current, transitionVariable):
    nextStates = []
    newStates2 = []
    if (current, transitionVariable) in states:
        nextStates = states[(current, transitionVariable)]
        for state in nextStates:
            if state not in newStates2:
                newStates2.append(state)
        for state in newStates2:
            epsilonClosure = getEpsilonClosure(state)
            for newState in epsilonClosure:
                if newState not in nextStates:
                    nextStates.append(newState)
    if not nextStates:
        return []
    return nextStates

def formatOutput(states):
    if states == ['#']:
        return '#'
    return ','.join(states)
def formatFinalOutput(StatesArr):
    return '|'.join(StatesArr)

if __name__ == "__main__":
    main()