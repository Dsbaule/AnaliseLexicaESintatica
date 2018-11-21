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
        self.states = set('S')
        self.transitions = dict()
        self.initial = 'S'
        self.final = set()
        self.tokenMap = dict()

        for index, afd in enumerate(afds):
            stateMap = dict()
            for state in afd.states:
                newState = str(index) + state
                stateMap[state] = newState
                self.addState(newState, afd.isFinal(state))
            for (stateFrom, symbol), stateTo in afd.transitions.items():
                self.addTransition(stateMap[stateFrom], symbol, stateMap[stateTo])
            self.addTransition('S', '&', stateMap[afd.initial])
            for state in afd.final:
                self.tokenMap[state] = afd.getTokenName()

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
        self.transitions.update({(stateFrom,symbol):{stateTo}})

    def addTransition(self, stateFrom, symbol, stateTo):
        if stateFrom not in self.states:
            raise NameError('Invalid starting State!' + stateFrom)
        if stateTo not in self.states:
            raise NameError('Invalid end State!: ' + stateTo)
        transition = self.transitions.get((stateFrom, symbol), None)
        if transition is None:
            self.transitions[(stateFrom, symbol)] = {stateTo}
        else:
            transition.add(stateTo)

    def setTransitions(self, stateFrom, symbols, stateTo):
        for symbol in symbols:
            self.setTransition(stateFrom, symbol, stateTo)

    def accepts(self, word):
        last_accept = 0
        accepting_states = set()

        steps = 0

        current_states = self.getEpsilonClosure({self.initial})
        for symbol in word:
            steps += 1
            next_states = set()
            for state in current_states:
                next_state = self.transitions.get((state, symbol), None)
                if next_state is not None:
                    next_states.update(next_state)
            current_states = self.getEpsilonClosure(next_states)
            cur_accepting_states = current_states.intersection(self.final)
            if cur_accepting_states is not set():
                last_accept = steps
                accepting_states = cur_accepting_states.copy()

        return (last_accept, [self.tokenMap[state] for state in accepting_states], accepting_states)

    def getEpsilonClosure(self, states):
        new_states = states
        while True:
            old_states = new_states
            for state in old_states:
                new_states = new_states.union(self.transitions.get((state, '&'), {}))
            if new_states == old_states:
                break
        return new_states

    def clear(self):
        self.states = set()
        self.transitions = dict()
        self.initial = None
        self.final = set()
