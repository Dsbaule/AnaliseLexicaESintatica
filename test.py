import GrammarReader

file = open('.\\Grammar.txt', 'r')
string = file.read()
file.close()

# newString = readGrammar('<stmt> ::= <loc> = <bool> ; | <if> | while ( <bool> ) <stmt> | do <stmt> while ( <bool> ) ; | break ; | <block>')
grammar = GrammarReader.readGrammar(string)
print(str(grammar))
