'''
Context Free Grammar Reader
    Reads a context free grammar from a stringself.
    Each Non-Terminal should ocupy a single line, with productions separated by '|'.
    Each symbol should be separated by a whitespace (' ').
    Epsilon should be written as '&'
    Example:
        <stmt> ::= <loc> = <bool> ; | <if> | while ( <bool> ) <stmt> | do <stmt> while ( <bool> ) ; | break ; | <block>
'''

def readGrammar(string):

    alphabet = set()
    nonTerminals = set()
    terminals = set()
    productions = dict()

    lines = string.split('\n')
    for line in lines:
        symbols = [x for x in line.split(' ') if x != '::=']
        nonTerminal = symbols[0]
        if nonTerminal is '':
            continue
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


    print(str(symbols))
    print(str(nonTerminals))
    print(str(terminals))
    print ("{:<15} {:<100}".format('NaoTerminal','Producao'))
    for k, v in productions.items():
        print ("{:<15} {:<100}".format(k, str(v[0])))
        if len(v) > 1:
            for value in v[1:]:
                print ("{:<15} {:<100}".format(' ', str(value)))


file = open('.\\Grammar.txt', 'r')
string = file.read()
file.close()

# newString = readGrammar('<stmt> ::= <loc> = <bool> ; | <if> | while ( <bool> ) <stmt> | do <stmt> while ( <bool> ) ; | break ; | <block>')
newString = readGrammar(string)
print(string)
