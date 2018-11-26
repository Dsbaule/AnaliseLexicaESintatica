from lex import lexAnaliser

class Parser:

    def __init__(self, grammar, lexAnaliser):
        self.lexAnaliser = lexAnaliser
        self.grammar = grammar
        self.parsingTable = self.grammar.getParsingTable()
        self.lineCount = 0

    def getParsingTree(self, string):
        self.lineCount = 0
        self.lexAnaliser.setInput(string)
        nextToken = self.getNextToken()

        parsingTree = list()

        stack = list()
        stack.append('$')
        currentSymbol = self.grammar.startingSymbol

        while(nextToken != '$' or currentSymbol != '$'):
            if currentSymbol is '&':
                currentSymbol = stack.pop()
            elif currentSymbol in self.grammar.nonTerminals:
                production = self.parsingTable[currentSymbol][nextToken]
                if len(production) is 0:
                    parsingTree.append((nextToken, ['Error in line ' + str(self.lineCount)]))
                    break
                production = production[0]
                parsingTree.append((currentSymbol, production))
                currentSymbol = production[0]
                prod = production[1:].copy()
                prod.reverse()
                stack.extend(prod)
            else:
                if currentSymbol == nextToken:
                    currentSymbol = stack.pop()
                    nextToken = self.getNextToken()
                else:
                    parsingTree.append((nextToken, ['Error in line ' + str(self.lineCount)]))
                    break
        return parsingTree

    def getNextToken(self):
        while True:
            (tokenLength, token) = self.lexAnaliser.getNextToken()
            if token is 'nl':
                self.lineCount += 1
                continue
            if token in ['ws','tb']:
                continue
            return token
