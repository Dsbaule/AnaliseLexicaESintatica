'''
Context Free Grammar Reader
    Reads a context free grammar from a stringself.
    Each Non-Terminal should ocupy a single line, with productions separated by '|'.
    Each symbol should be separated by a whitespace (' ').
    Epsilon should be written as '&'
    Example:
        <stmt> ::= <loc> = <bool> ; | <if> | while ( <bool> ) <stmt> | do <stmt> while ( <bool> ) ; | break ; | <block>
'''

from CFG import CFG

def readGrammar(string):

    alphabet = set()
    nonTerminals = set()
    terminals = set()
    productions = dict()
    startingSymbol = None

    lines = string.split('\n')
    for line in lines:
        symbols = [x for x in line.split(' ') if x != '::=']
        nonTerminal = symbols[0]
        if nonTerminal is '':
            continue
        if startingSymbol is None:
            startingSymbol = nonTerminal
        nonTerminals.add(nonTerminal)
        currentProductions = productions.get(nonTerminal, list())
        production = list()
        for symbol in symbols[1:]:
            if symbol is '|':
                currentProductions.append(production)
                production = list()
                continue
            alphabet.add(symbol)
            production.append(symbol)
        currentProductions.append(production)
        productions[nonTerminal] = currentProductions

    terminals = alphabet.difference(nonTerminals)

    return CFG(startingSymbol, terminals, nonTerminals, productions)

file = open('.\\Grammar.txt', 'r')
string = file.read()
file.close()

# newString = readGrammar('<stmt> ::= <loc> = <bool> ; | <if> | while ( <bool> ) <stmt> | do <stmt> while ( <bool> ) ; | break ; | <block>')
grammar = readGrammar(string)
print(str(grammar))
