from AFD import AFD
import CharClasses

# AFD for token (
def OP_AFD():
    afd = getStringAFD('(')
    afd.setTokenName('(')
    return afd

# AFD for token )
def CP_AFD():
    #print( str(getStringAFD(')')))
    afd = getStringAFD(')')
    afd.setTokenName(')')
    return afd

# AFD for token [
def OB_AFD():
    afd = getStringAFD('[')
    afd.setTokenName('[')
    return afd

# AFD for token ]
def CB_AFD():
    afd = getStringAFD(']')
    afd.setTokenName(']')
    return afd

# AFD for token {
def OCB_AFD():
    afd = getStringAFD('{')
    afd.setTokenName('{')
    return afd

# AFD for token }
def CCB_AFD():
    afd = getStringAFD('}')
    afd.setTokenName('}')
    return afd

# AFD for token ;
def SC_AFD():
    afd = getStringAFD(';')
    afd.setTokenName(';')
    return afd

# AFD for token ||
def OR_AFD():
    afd = getStringAFD('||')
    afd.setTokenName('||')
    return afd

# AFD for token &&
def AND_AFD():
    afd = getStringAFD('&&')
    afd.setTokenName('&&')
    return afd

# AFD for token ==
def EQ_AFD():
    afd = getStringAFD('==')
    afd.setTokenName('==')
    return afd

# AFD for token !=
def NEQ_AFD():
    afd = getStringAFD('!=')
    afd.setTokenName('!=')
    return afd

# AFD for token <
def LT_AFD():
    afd = getStringAFD('<')
    afd.setTokenName('<')
    return afd

# AFD for token <=
def LE_AFD():
    afd = getStringAFD('<=')
    afd.setTokenName('<=')
    return afd

# AFD for token >=
def GE_AFD():
    afd = getStringAFD('>=')
    afd.setTokenName('>=')
    return afd

# AFD for token >
def GT_AFD():
    afd = getStringAFD('>')
    afd.setTokenName('>')
    return afd

# AFD for token =
def ATT_AFD():
    afd = getStringAFD('=')
    afd.setTokenName('=')
    return afd

# AFD for token +
def PL_AFD():
    afd = getStringAFD('+')
    afd.setTokenName('+')
    return afd

# AFD for token -
def MN_AFD():
    afd = getStringAFD('-')
    afd.setTokenName('-')
    return afd

# AFD for token *
def MT_AFD():
    afd = getStringAFD('*')
    afd.setTokenName('*')
    return afd

# AFD for token /
def DV_AFD():
    afd = getStringAFD('/')
    afd.setTokenName('/')
    return afd

# AFD for token !
def NOT_AFD():
    afd = getStringAFD('!')
    afd.setTokenName('!')
    return afd

# AFD for token if
def if_AFD():
    afd = getStringAFD('if')
    afd.setTokenName('if')
    return afd

# AFD for token then
def then_AFD():
    afd = getStringAFD('then')
    afd.setTokenName('then')
    return afd

# AFD for token else
def else_AFD():
    afd = getStringAFD('else')
    afd.setTokenName('else')
    return afd

# AFD for token while
def while_AFD():
    afd = getStringAFD('while')
    afd.setTokenName('while')
    return afd

# AFD for token do
def do_AFD():
    afd = getStringAFD('do')
    afd.setTokenName('do')
    return afd

# AFD for token break
def break_AFD():
    afd = getStringAFD('break')
    afd.setTokenName('break')
    return afd

# AFD for token num ([0-9])
def num_AFD():
    num_AFD = AFD()
    num_AFD.addState('', False, True)
    num_AFD.addState('num', True)
    num_AFD.setTransitions('', CharClasses.digits(), 'num')
    num_AFD.setTransitions('num', CharClasses.digits(), 'num')
    num_AFD.setTokenName('num')
    return num_AFD

# AFD for token real ([0-9].[0-9])
def real_AFD():
    real_AFD = AFD()
    real_AFD.addState('', False, True)
    real_AFD.addState('num')
    real_AFD.addState('num.')
    real_AFD.addState('num.num', True)
    real_AFD.setTransitions('', CharClasses.digits(), 'num')
    real_AFD.setTransitions('num', CharClasses.digits(), 'num')
    real_AFD.setTransitions('num', '.', 'num.')
    real_AFD.setTransitions('num.', CharClasses.digits(), 'num.num')
    real_AFD.setTransitions('num.num', CharClasses.digits(), 'num.num')
    real_AFD.setTokenName('real')
    return real_AFD

# AFD for token true
def true_AFD():
    afd = getStringAFD('true')
    afd.setTokenName('bool')
    return afd

# AFD for token false
def false_AFD():
    afd = getStringAFD('false')
    afd.setTokenName('bool')
    return afd

# AFD for token id
def id_AFD():
    idAFD = AFD()
    idAFD.addState('', False, True)
    idAFD.addState('char', True)
    idAFD.setTransitions('', CharClasses.letters(), 'char')
    idAFD.setTransitions('char', CharClasses.letters(), 'char')
    idAFD.setTransitions('char', CharClasses.digits(), 'char')
    idAFD.setTokenName('id')
    return idAFD

# AFD for new line
def nl_AFD():
    afd = getStringAFD('\n')
    afd.setTokenName('nl')
    return afd

# AFD for whitespace (space and tab)
def ws_AFD():
    afd = getStringAFD(' ')
    afd.setTokenName('ws')
    return afd

# AFD for whitespace (space and tab)
def tb_AFD():
    afd = getStringAFD('\t')
    afd.setTokenName('tb')
    return afd

'''
    !!!!!!!!!!!!!!!!!!!!!!!!!!! VERIFICAR BASIC !!!!!!!!!!!!!!!!!!!!!!!!!!
'''
# AFD for token basic
def basic_AFD():
    afd = getStringAFD('basic')
    afd.setTokenName('basic')
    return afd

def getStringAFD(string):
    afd = AFD()
    afd.addState('', False, True)
    lastString = ''
    for char in string:
        newString = lastString + char
        afd.addState(newString)
        afd.setTransition(lastString, char, newString)
        lastString = newString
    afd.setFinal(lastString)
    return afd
