import GrammarReader
from lex import lexAnaliser

file = open('.\\Grammar.txt', 'r')
string = file.read()
file.close()

# newString = readGrammar('<stmt> ::= <loc> = <bool> ; | <if> | while ( <bool> ) <stmt> | do <stmt> while ( <bool> ) ; | break ; | <block>')
grammar = GrammarReader.readGrammar(string)
lex = lexAnaliser()
lex.setInput()
print(str(grammar))
