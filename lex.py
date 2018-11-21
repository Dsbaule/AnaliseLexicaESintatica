import TokenAFDs

class lexAnaliser:

    def __init__(self):
        self.OP_AFD = TokenAFDs.OP_AFD()
        self.CP_AFD = TokenAFDs.CP_AFD()
        self.OB_AFD = TokenAFDs.OB_AFD()
        self.CB_AFD = TokenAFDs.CB_AFD()
        self.OCB_AFD = TokenAFDs.OCB_AFD()
        self.CCB_AFD = TokenAFDs.CCB_AFD()
        self.SC_AFD = TokenAFDs.SC_AFD()
        self.OR_AFD = TokenAFDs.OR_AFD()
        self.AND_AFD = TokenAFDs.AND_AFD()
        self.EQ_AFD = TokenAFDs.EQ_AFD()
        self.NEQ_AFD = TokenAFDs.NEQ_AFD()
        self.LT_AFD = TokenAFDs.LT_AFD()
        self.LE_AFD = TokenAFDs.LE_AFD()
        self.GE_AFD = TokenAFDs.GE_AFD()
        self.GT_AFD = TokenAFDs.GT_AFD()
        self.ATT_AFD = TokenAFDs.ATT_AFD()
        self.PL_AFD = TokenAFDs.PL_AFD()
        self.MN_AFD = TokenAFDs.MN_AFD()
        self.MT_AFD = TokenAFDs.MT_AFD()
        self.DV_AFD = TokenAFDs.DV_AFD()
        self.NOT_AFD = TokenAFDs.NOT_AFD()
        self.if_AFD = TokenAFDs.if_AFD()
        self.then_AFD = TokenAFDs.then_AFD()
        self.else_AFD = TokenAFDs.else_AFD()
        self.while_AFD = TokenAFDs.while_AFD()
        self.do_AFD = TokenAFDs.do_AFD()
        self.break_AFD = TokenAFDs.break_AFD()
        self.num_AFD = TokenAFDs.num_AFD()
        self.real_AFD = TokenAFDs.real_AFD()
        self.true_AFD = TokenAFDs.true_AFD()
        self.false_AFD = TokenAFDs.false_AFD()
        self.id_AFD = TokenAFDs.id_AFD()
        self.basic_AFD = TokenAFDs.basic_AFD()
        self.nl_AFD = TokenAFDs.nl_AFD()
        self.ws_AFD = TokenAFDs.ws_AFD()
        self.tb_AFD = TokenAFDs.tb_AFD()

    def getNextToken(self, string):
        longesttoken = 0
        token = 'Error'

        tokensize = self.OP_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '('
        tokensize = self.CP_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = ')'
        tokensize = self.OB_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '['
        tokensize = self.CB_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = ']'
        tokensize = self.OCB_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '{'
        tokensize = self.CCB_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '}'
        tokensize = self.SC_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = ';'
        tokensize = self.OR_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '||'
        tokensize = self.AND_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '&&'
        tokensize = self.EQ_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '=='
        tokensize = self.NEQ_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '!='
        tokensize = self.LT_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '<'
        tokensize = self.LE_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '<='
        tokensize = self.GE_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '>='
        tokensize = self.GT_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '>'
        tokensize = self.ATT_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '='
        tokensize = self.PL_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '+'
        tokensize = self.MN_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '-'
        tokensize = self.MT_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '*'
        tokensize = self.DV_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '/'
        tokensize = self.NOT_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = '!'
        tokensize = self.if_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'if'
        tokensize = self.then_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'then'
        tokensize = self.else_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'else'
        tokensize = self.while_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'while'
        tokensize = self.do_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'do'
        tokensize = self.break_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'break'
        tokensize = self.num_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'num'
        tokensize = self.real_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'real'
        tokensize = self.true_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'true'
        tokensize = self.false_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'false'
        tokensize = self.basic_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'basic'
        tokensize = self.id_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'id'
        tokensize = self.nl_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'nl'
        tokensize = self.ws_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'ws'
        tokensize = self.tb_AFD.accepts(string)
        if tokensize > longesttoken:
            longesttoken = tokensize
            token = 'tb'

        return (longesttoken, token)


buffersize = 256 # buffersize in characters

tokens = list()
codigo = """{
    basic[19][18] = 15.26666;
    if (test==19) then
        test = 15.36
    else
        test = test + test
}"""

length = len(codigo)
index = 0

lex = lexAnaliser()

while(index < length):
    tokenlength, token = lex.getNextToken(codigo[index:(index + buffersize)])
    if tokenlength is 0:
        print("TOKEN INVALIDO ENCONTRADO")
        break
    index += tokenlength
    tokens.append(token)

printable = ""
for token in tokens:
    if token is 'ws':
        printable += ' '
    elif token is 'tb':
        printable += '\t'
    elif token is 'nl':
        printable += '\n'
    else:
        printable += token

print(codigo)
print(printable)
