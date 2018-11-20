import TokenAFDs
from AFD import AFD

print("Testing generated AFDs:")

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")

assert (TokenAFDs.CP_AFD().accepts(')asd') > 0)
assert (TokenAFDs.CP_AFD().accepts('(a)els)') == 0)
print("TEST TOKEN )     ->  OK")

assert (TokenAFDs.OB_AFD().accepts('[asd]') > 0)
assert (TokenAFDs.OB_AFD().accepts('a[els)') == 0)
print("TEST TOKEN [     ->  OK")

assert (TokenAFDs.CB_AFD().accepts(']dsa') > 0)
assert (TokenAFDs.CB_AFD().accepts('a])') == 0)
print("TEST TOKEN ]     ->  OK")

assert (TokenAFDs.OCB_AFD().accepts('{ASD}') > 0)
assert (TokenAFDs.OCB_AFD().accepts('({els)') == 0)
print("TEST TOKEN {     ->  OK")

assert (TokenAFDs.CCB_AFD().accepts('}') > 0)
assert (TokenAFDs.CCB_AFD().accepts('{}els)') == 0)
print("TEST TOKEN }     ->  OK")

'''

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token ;
def SC_AFD():
    return getStringAFD(';')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token ||
def OR_AFD():
    return getStringAFD('||')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token &&
def AND_AFD():
    return getStringAFD('&&')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token ==
def EQ_AFD():
    return getStringAFD('==')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token !=
def NEQ_AFD():
    return getStringAFD('!=')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token <
def LT_AFD():
    return getStringAFD('<')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token <=
def LE_AFD():
    return getStringAFD('<=')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token >=
def GE_AFD():
    return getStringAFD('>=')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token >
def GT_AFD():
    return getStringAFD('>')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token =
def ATT_AFD():
    return getStringAFD('=')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token +
def PL_AFD():
    return getStringAFD('+')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token -
def MN_AFD():
    return getStringAFD('-')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token *
def MT_AFD():
    return getStringAFD('*')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token /
def DV_AFD():
    return getStringAFD('/')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token !
def NOT_AFD():
    return getStringAFD('!')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token if
def if_AFD():
    return getStringAFD('if')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token then
def then_AFD():
    return getStringAFD('then')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token else
def else_AFD():
    return getStringAFD('else')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token while
def while_AFD():
    return getStringAFD('while')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token do
def do_AFD():
    return getStringAFD('do')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token break
def break_AFD():
    return getStringAFD('break')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token num ([0-9])
def num_AFD():
    num_AFD = AFD()
    num_AFD.addState('', False, True)
    num_AFD.addState('num', True)
    num_AFD.setTransitions('', CharClasses.digits(), 'num')
    num_AFD.setTransitions('num', CharClasses.digits(), 'num')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token real ([0-9].[0-9])
def real_AFD():
    real_AFD = AFD()
    real_AFD.addState('', False, True)
    real_AFD.addState('num')
    real_AFD.addState('num.')
    real_AFD.addState('num.number')
    real_AFD.setTransitions('', CharClasses.digits(), 'num')
    real_AFD.setTransitions('num', CharClasses.digits(), 'num')
    real_AFD.setTransitions('num', '.', 'num.')
    real_AFD.setTransitions('num.', CharClasses.digits(), 'num.num')
    real_AFD.setTransitions('num.num', CharClasses.digits(), 'num.num')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token true
def true_AFD():
    return getStringAFD('true')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token false
def false_AFD():
    return getStringAFD('false')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token id
def id_AFD():
    idAFD = AFD()
    idAFD.addState('', False, True)
    idAFD.addState('char', True)
    idAFD.setTransitions('', CharClasses.letters(), 'char')
    idAFD.setTransitions('char', CharClasses.letters(), 'char')
    idAFD.setTransitions('char', CharClasses.digits(), 'char')

assert (TokenAFDs.OP_AFD().accepts('(') > 0)
assert (TokenAFDs.OP_AFD().accepts('a(els)') == 0)
print("TEST TOKEN (     ->  OK")
# AFD for token basic
def basic_AFD():
    return getStringAFD('basic')
    '''
