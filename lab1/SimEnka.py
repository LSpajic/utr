import sys
from collections import defaultdict

states = {}

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
    #
    # Uzet input
    # krece parsiranje
    #
    #print("--------------------")
    for input_string in inputStrings:
        currState = []
        currState += getEpsilonClosure(startState, states)
        currState.sort()
        tmpState = []
        output = []
        output.append(formatOutput(currState))
        #print(formatOutput(currState), end='')
        for transVariable in input_string:
            #print(transVariable)
            for state in currState:
                tmpState += getNextStates(state, transVariable, states)
            currState = tmpState
            tmpState = []
            if currState == []:
                currState = ['#']
            currState = list(set(currState))
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

def getEpsilonClosure(current, states):
    epsilonClosure = []
    epsilonClosure.append(current)
    tmpState = []
    for state in epsilonClosure:
        if (state, '$') in states:
            tmpState = states[(state, '$')]
            for newState in tmpState:
                if newState not in epsilonClosure:
                    epsilonClosure.append(newState)
    return epsilonClosure
    
def getNextStates(current, transitionVariable, states):
    nextStates = []
    newStates2 = []
    if (current, transitionVariable) in states:
        nextStates = states[(current, transitionVariable)]
        for state in nextStates:
            if state not in newStates2:
                newStates2.append(state)
        for state in newStates2:
            epsilonClosure = getEpsilonClosure(state, states)
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

if __name__ == main():
    main()