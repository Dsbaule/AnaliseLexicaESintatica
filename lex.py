import TokenAFDs


def getNextToken(string):
    longesttoken = 0
    token = 'Error'

    tokensize = OP_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '('
    tokensize = CP_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = ')'
    tokensize = OB_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '['
    tokensize = CB_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = ']'
    tokensize = OCB_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '{'
    tokensize = CCB_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '}'
    tokensize = SC_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = ';'
    tokensize = OR_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '||'
    tokensize = AND_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '&&'
    tokensize = EQ_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '=='
    tokensize = NEQ_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '!='
    tokensize = LT_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '<'
    tokensize = LE_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '<='
    tokensize = GE_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '>='
    tokensize = GT_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '>'
    tokensize = ATT_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '='
    tokensize = PL_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '+'
    tokensize = MN_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '-'
    tokensize = MT_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '*'
    tokensize = DV_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '/'
    tokensize = NOT_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = '!'
    tokensize = if_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = 'if'
    tokensize = then_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = 'then'
    tokensize = else_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = 'else'
    tokensize = while_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = 'while'
    tokensize = do_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = 'do'
    tokensize = break_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = 'break'
    tokensize = num_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = 'num'
    tokensize = real_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = 'real'
    tokensize = true_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = 'true'
    tokensize = false_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = 'false'
    tokensize = basic_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = 'basic'
    tokensize = id_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = 'id'
    tokensize = nl_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = 'nl'
    tokensize = ws_AFD.accepts(string)
    if tokensize > longesttoken:
        longesttoken = tokensize
        token = 'ws'
    tokensize = tb_AFD.accepts(string)
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

OP_AFD = TokenAFDs.OP_AFD()
CP_AFD = TokenAFDs.CP_AFD()
OB_AFD = TokenAFDs.OB_AFD()
CB_AFD = TokenAFDs.CB_AFD()
OCB_AFD = TokenAFDs.OCB_AFD()
CCB_AFD = TokenAFDs.CCB_AFD()
SC_AFD = TokenAFDs.SC_AFD()
OR_AFD = TokenAFDs.OR_AFD()
AND_AFD = TokenAFDs.AND_AFD()
EQ_AFD = TokenAFDs.EQ_AFD()
NEQ_AFD = TokenAFDs.NEQ_AFD()
LT_AFD = TokenAFDs.LT_AFD()
LE_AFD = TokenAFDs.LE_AFD()
GE_AFD = TokenAFDs.GE_AFD()
GT_AFD = TokenAFDs.GT_AFD()
ATT_AFD = TokenAFDs.ATT_AFD()
PL_AFD = TokenAFDs.PL_AFD()
MN_AFD = TokenAFDs.MN_AFD()
MT_AFD = TokenAFDs.MT_AFD()
DV_AFD = TokenAFDs.DV_AFD()
NOT_AFD = TokenAFDs.NOT_AFD()
if_AFD = TokenAFDs.if_AFD()
then_AFD = TokenAFDs.then_AFD()
else_AFD = TokenAFDs.else_AFD()
while_AFD = TokenAFDs.while_AFD()
do_AFD = TokenAFDs.do_AFD()
break_AFD = TokenAFDs.break_AFD()
num_AFD = TokenAFDs.num_AFD()
real_AFD = TokenAFDs.real_AFD()
true_AFD = TokenAFDs.true_AFD()
false_AFD = TokenAFDs.false_AFD()
id_AFD = TokenAFDs.id_AFD()
basic_AFD = TokenAFDs.basic_AFD()
nl_AFD = TokenAFDs.nl_AFD()
ws_AFD = TokenAFDs.ws_AFD()
tb_AFD = TokenAFDs.tb_AFD()

length = len(codigo)
index = 0
while(index < length):
    tokenlength, token = getNextToken(codigo[index:(index + buffersize)])
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
