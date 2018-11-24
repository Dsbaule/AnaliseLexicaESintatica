
class CFG:
    def __init__(self, startingSymbol, terminals, nonTerminals, productions):
        self.startingSymbol = startingSymbol
        self.terminals = terminals
        self.nonTerminals = nonTerminals
        self.productions = productions

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
        string += '\n'
        return string
