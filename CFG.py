
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
        for symbol in self.nonTerminals:
            self.follow[symbol] = set()
        self.follow[self.startingSymbol].add('$')

        self.parsingTable = dict()
        for nonTerminal in self.nonTerminals:
            self.parsingTable[nonTerminal] = dict()
            for terminal in self.terminals:
                self.parsingTable[nonTerminal][terminal] = list()
            self.parsingTable[nonTerminal]['$'] = list()

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
        string += '\nFirsts:\n'
        for nonTerminal in self.nonTerminals:
            string += "\t{:<15} {:<80}\n".format(nonTerminal, str(self.first[nonTerminal]))
        string += '\n'
        string += '\nFollows:\n'
        for nonTerminal in self.nonTerminals:
            string += "\t{:<15} {:<80}\n".format(nonTerminal, str(self.follow[nonTerminal]))
        string += '\n'
        string += 'Parsing Table:\n'

        string += "\t{:<15}".format(' ')
        for terminal in self.terminals:
            string += "{:<30}".format(terminal)
        string += "{:<30}".format('$')
        for nonTerminal in self.nonTerminals:
            string += "\n\t{:<15}".format(nonTerminal)
            for terminal in self.terminals:
                string += "{:<30}".format(str(self.parsingTable[nonTerminal][terminal]))
            string += "{:<30}".format(str(self.parsingTable[nonTerminal]['$']))

        return string

    def generateTable(self):
        self.generateFirst()
        self.generateFollow()

        for nonTerminal, productions in self.productions.items():
            for production in productions:
                first = self.getProductionFirst(production)
                for symbol in first:
                    if symbol is '&':
                        for symbol in self.follow[nonTerminal]:
                            self.parsingTable[nonTerminal][symbol].append(production)
                    else:
                        self.parsingTable[nonTerminal][symbol].append(production)



    def generateFirst(self):
        oldFirst = dict()

        while(True):
            done = True
            oldFirst.clear()
            for nonTerminal in self.nonTerminals:
                oldFirst[nonTerminal] = self.first[nonTerminal].copy()
            for nonTerminal, productions in self.productions.items():
                for production in productions:
                    for index in range(len(production) + 1):
                        if index >= len(production):
                            self.first[nonTerminal].add('&')
                            break
                        first = self.getSymbolFirst(production[index])
                        self.first[nonTerminal].update(first - {'&'})
                        if '&' not in first:
                            break
            for nonTerminal in self.nonTerminals:
                if oldFirst[nonTerminal] != self.first[nonTerminal]:
                    done = False
                    break
            if done:
                break

    def generateFollow(self):
        oldFollow = dict()

        while(True):
            done = True
            oldFollow.clear()
            for nonTerminal in self.nonTerminals:
                oldFollow[nonTerminal] = self.follow[nonTerminal].copy()

            for nonTerminal, productions in self.productions.items():
                for production in productions:
                    for i in range(len(production) - 1):
                        if production[i] in self.nonTerminals:
                            for j in range(i + 1,len(production) + 1):
                                if j is len(production):
                                    self.follow[production[i]].update(self.follow[nonTerminal])
                                    break
                                first = self.getSymbolFirst(production[j])
                                self.follow[production[i]].update(first - {'&'})
                                if '&' not in first:
                                    break;
                    if production[-1] in self.nonTerminals:
                        self.follow[production[-1]].update(self.follow[nonTerminal])


            for nonTerminal in self.nonTerminals:
                if oldFollow[nonTerminal] != self.follow[nonTerminal]:
                    done = False
                    break
            if done:
                break

    def getSymbolFirst(self, symbol):
        if symbol in self.terminals or symbol is '&':
            return {symbol}
        return self.first[symbol]

    def getProductionFirst(self, production):
        productionFirst = set()
        for index in range(len(production) + 1):
            if index >= len(production):
                productionFirst.add('&')
                break
            first = self.getSymbolFirst(production[index])
            productionFirst.update(first - {'&'})
            if '&' not in first:
                break
        return productionFirst

    def getFirst(self):
        return self.first

    def getFollow(self):
        return self.follow

    def getParsingTable(self):
        return self.parsingTable
