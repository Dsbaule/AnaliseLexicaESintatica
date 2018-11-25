
class CFG:
    def __init__(self, startingSymbol, terminals, nonTerminals, productions):
        self.startingSymbol = startingSymbol
        self.terminals = terminals
        self.nonTerminals = nonTerminals
        self.productions = productions
        self.first = dict()
        for symbol in self.nonTerminals:
            self.first[symbol] = set()
        self.follow = dict()
        self.table = dict()
        self.generateTable()

    def __str__(self):
        string =  \
            'Terminals: ' + str(self.terminals) + '\n\n' \
            'Non-Terminals: ' + str(self.nonTerminals) + '\n\n' \
            'Productions:\n\n' + \
            "\t{:<15} {:<100}\n\n".format('Non-Terminal','Production')
        for key, value in self.productions.items():
            string += "\t{:<15} ".format(key)
            for symbol in value[0]:
                string += symbol + ' '
            string += '\n'
            if len(value) > 1:
                for prod in value[1:]:
                    string += "\t{:<15} ".format(' ')
                    for symbol in prod:
                        string += symbol + ' '
                    string += '\n'
        string += '\nFirsts:'
        for nonTerminal in self.nonTerminals:
            string += "\t{:<15} {:<80}\n".format(nonTerminal, str(self.first[nonTerminal]))
        string += '\n'
        return string

    def generateTable(self):
        self.generateFirst()
        #self.generateFollow()

    def generateFirst(self):
        oldFirst = dict()

        while(True):
            done = True
            oldFirst.clear()
            for nonTerminal in self.nonTerminals:
                oldFirst[nonTerminal] = self.first[nonTerminal].copy()
            for nonTerminal, productions in self.productions.items():
                for production in productions:
                    for symbol in production:
                        first = self.getSymbolFirst(symbol)
                        # print("\t{:<15} {:<30} {:<100}\n".format(nonTerminal, symbol, str(first)))
                        self.first[nonTerminal].update(first)
                        if '&' not in first:
                            break
            for nonTerminal in self.nonTerminals:
                if oldFirst[nonTerminal] != self.first[nonTerminal]:
                    done = False
                    break
            if done:
                break

    def getSymbolFirst(self, symbol):
        if symbol in self.terminals or symbol is '&':
            return {symbol}
        return self.first[symbol]

    def getFirst(self):
        return self.first

    def getFollow(self):
        return self.follow
