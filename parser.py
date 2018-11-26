from lex import lexAnaliser

class Parser():
    def __init__(self, grammar, lexAnaliser):
        self.lexAnaliser = lexAnaliser
        self.grammar = grammar
        self.parsingTable = self.grammar.getParsingTable()

    def getParsingTree(self):
        nextToken = self.lexAnaliser.getNextToken()

        stack = list()
        stack.append('$')
        currentSymbol = self.grammar.startingSymbol

        parsingTree = list()

        while(nextToken != '$' or currentSymbol != '$'):
            if currentSymbol in self.grammar.terminals:
                if currentSymbol == nextToken:
                    currentSymbol = stack.pop()
                    nextToken = self.lexAnaliser.getNextToken()
                    continue
                else:
                    parsingTree.append((nextToken, 'Error'))

            production = self.parsingTable[nextToken]
