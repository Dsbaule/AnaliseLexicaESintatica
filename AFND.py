from AFD import AFD

class AFND:
    '''
    A Finite Automata FA is a quintuple (Q, E, T, S, F), where:
    Q is the set of states             (not necessary)
    E is the set of symbols            (not necessary)
    T is the set of transition rules   (not necessary)
    S is the start state               (necessary)
    F is the final/accepting state     (necessary)
    '''
    def __init__(self, afds):
        self.addState('S', False, True)
        for index, afd in enumerate(afds):
            self.setTransition('S', '&', str(index) + afd.initial):
            stateMap = dict()
            for state in afd.states:
                newState = str(index) + state
                stateMap[state] = newState
                self.addState(newState, afd.isFinal(state))
            for (stateFrom, symbol), stateTo in afd.transitions.items():
                self.setTransition(stateMap[stateFrom], symbol, stateMap[stateTo])

    def __str__(self):
        return \
        ('States: ' + str(self.states) + '\n' + \
        'Transitions: ' + str(self.transitions)  + '\n' + \
        'Initial: ' + str(self.initial)  + '\n' + \
        'Final: ' + str(self.final))

    def addState(self, state, final = False, initial = False):
        self.states.add(state)
        if final:
            self.final.add(state)
        if initial or self.initial == None:
            self.initial = state

    def removeState(self, state):
        if state not in self.states:
            raise NameError('Invalid State: ' + state)
        if self.initial == state:
            self.initial = None
        self.states.discard(state)
        self.final.discard(state)

    def setFinal(self, state):
        if state not in self.states:
            raise NameError('Invalid State: ' + state)
        self.final.add(state)

    def setNotFinal(self, state):
        if state not in self.states:
            raise NameError('Invalid State: ' + state)
        self.final.discard(state)

    def setInitial(self, state):
        if state not in self.states:
            raise NameError('Invalid State: ' + state)
        self.initial = state

    def setTransition(self, stateFrom, symbol, stateTo):
        if stateFrom not in self.states:
            raise NameError('Invalid starting State!' + stateFrom)
        if stateTo not in self.states:
            raise NameError('Invalid end State!: ' + stateTo)
        self.transitions.update({(stateFrom,symbol):stateTo})

    def setTransitions(self, stateFrom, symbols, stateTo):
        for symbol in symbols:
            self.setTransition(stateFrom, symbol, stateTo)

    def accepts(self, word):
        last_accept = 0
        steps = 0
        current_state = self.initial
        for symbol in word:
            current_state = self.transitions.get((current_state, symbol), None)
            steps += 1
            if current_state not in self.states:
                 return last_accept
            if current_state in self.final:
                last_accept = steps
        return last_accept

    def clear(self):
        self.states = set()
        self.transitions = dict()
        self.initial = None
        self.final = set()
