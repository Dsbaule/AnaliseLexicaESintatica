from AFD import AFD
import CharClasses

# AFD for token (
def OP_AFD():
    return getStringAFD('(')

# AFD for token )
def CP_AFD():
    #print( str(getStringAFD(')')))
    return getStringAFD(')')

# AFD for token [
def OB_AFD():
    return getStringAFD('[')

# AFD for token ]
def CB_AFD():
    return getStringAFD(']')

# AFD for token {
def OCB_AFD():
    return getStringAFD('{')

# AFD for token }
def CCB_AFD():
    return getStringAFD('}')

# AFD for token ;
def SC_AFD():
    return getStringAFD(';')

# AFD for token ||
def OR_AFD():
    return getStringAFD('||')

# AFD for token &&
def AND_AFD():
    return getStringAFD('&&')

# AFD for token ==
def EQ_AFD():
    return getStringAFD('==')

# AFD for token !=
def NEQ_AFD():
    return getStringAFD('!=')

# AFD for token <
def LT_AFD():
    return getStringAFD('<')

# AFD for token <=
def LE_AFD():
    return getStringAFD('<=')

# AFD for token >=
def GE_AFD():
    return getStringAFD('>=')

# AFD for token >
def GT_AFD():
    return getStringAFD('>')

# AFD for token =
def ATT_AFD():
    return getStringAFD('=')

# AFD for token +
def PL_AFD():
    return getStringAFD('+')

# AFD for token -
def MN_AFD():
    return getStringAFD('-')

# AFD for token *
def MT_AFD():
    return getStringAFD('*')

# AFD for token /
def DV_AFD():
    return getStringAFD('/')

# AFD for token !
def NOT_AFD():
    return getStringAFD('!')

# AFD for token if
def if_AFD():
    return getStringAFD('if')

# AFD for token then
def then_AFD():
    return getStringAFD('then')

# AFD for token else
def else_AFD():
    return getStringAFD('else')

# AFD for token while
def while_AFD():
    return getStringAFD('while')

# AFD for token do
def do_AFD():
    return getStringAFD('do')

# AFD for token break
def break_AFD():
    return getStringAFD('break')

# AFD for token num ([0-9])
def num_AFD():
    num_AFD = AFD()
    num_AFD.addState('', False, True)
    num_AFD.addState('num', True)
    num_AFD.setTransitions('', CharClasses.digits(), 'num')
    num_AFD.setTransitions('num', CharClasses.digits(), 'num')
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
    return real_AFD

# AFD for token true
def true_AFD():
    return getStringAFD('true')

# AFD for token false
def false_AFD():
    return getStringAFD('false')

# AFD for token id
def id_AFD():
    idAFD = AFD()
    idAFD.addState('', False, True)
    idAFD.addState('char', True)
    idAFD.setTransitions('', CharClasses.letters(), 'char')
    idAFD.setTransitions('char', CharClasses.letters(), 'char')
    idAFD.setTransitions('char', CharClasses.digits(), 'char')
    return idAFD

# AFD for new line
def nl_AFD():
    return getStringAFD('\n')

# AFD for whitespace (space and tab)
def ws_AFD():
    return getStringAFD(' ')

# AFD for whitespace (space and tab)
def tb_AFD():
    return getStringAFD('\t')

'''
    !!!!!!!!!!!!!!!!!!!!!!!!!!! VERIFICAR BASIC !!!!!!!!!!!!!!!!!!!!!!!!!!
'''
# AFD for token basic
def basic_AFD():
    return getStringAFD('basic')

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
