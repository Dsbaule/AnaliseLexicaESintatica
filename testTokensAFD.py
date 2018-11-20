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

assert (TokenAFDs.CCB_AFD().accepts('}efda') > 0)
assert (TokenAFDs.CCB_AFD().accepts('{}els)') == 0)
print("TEST TOKEN }     ->  OK")

assert (TokenAFDs.SC_AFD().accepts(';ads') > 0)
assert (TokenAFDs.SC_AFD().accepts('asd;') == 0)
print("TEST TOKEN ;     ->  OK")

assert (TokenAFDs.OR_AFD().accepts('|| (test)') > 0)
assert (TokenAFDs.OR_AFD().accepts('|asd;') == 0)
print("TEST TOKEN ||    ->  OK")

assert (TokenAFDs.AND_AFD().accepts('&& (test)') > 0)
assert (TokenAFDs.AND_AFD().accepts('a(els)') == 0)
print("TEST TOKEN &&    ->  OK")

assert (TokenAFDs.EQ_AFD().accepts('== (test)') > 0)
assert (TokenAFDs.EQ_AFD().accepts('a == els)') == 0)
print("TEST TOKEN ==    ->  OK")

assert (TokenAFDs.NEQ_AFD().accepts('!= (test)') > 0)
assert (TokenAFDs.NEQ_AFD().accepts('a!=ls)') == 0)
print("TEST TOKEN !=    ->  OK")

assert (TokenAFDs.LT_AFD().accepts('<(test)') > 0)
assert (TokenAFDs.LT_AFD().accepts('a(<ls)') == 0)
print("TEST TOKEN <     ->  OK")

assert (TokenAFDs.LE_AFD().accepts('<=(test)') > 0)
assert (TokenAFDs.LE_AFD().accepts('a(<=ls)') == 0)
print("TEST TOKEN <=    ->  OK")

assert (TokenAFDs.GE_AFD().accepts('>=(test)') > 0)
assert (TokenAFDs.GE_AFD().accepts('a(>=ls)') == 0)
print("TEST TOKEN >=    ->  OK")

assert (TokenAFDs.GT_AFD().accepts('>(test)') > 0)
assert (TokenAFDs.GT_AFD().accepts('a(e>ls)') == 0)
print("TEST TOKEN >     ->  OK")

assert (TokenAFDs.ATT_AFD().accepts('= test') > 0)
assert (TokenAFDs.ATT_AFD().accepts('a(e=ls)') == 0)
print("TEST TOKEN =     ->  OK")

assert (TokenAFDs.PL_AFD().accepts('+test') > 0)
assert (TokenAFDs.PL_AFD().accepts('a(+els)') == 0)
print("TEST TOKEN +     ->  OK")

assert (TokenAFDs.MN_AFD().accepts('-test') > 0)
assert (TokenAFDs.MN_AFD().accepts('a(-els)') == 0)
print("TEST TOKEN -     ->  OK")

assert (TokenAFDs.MT_AFD().accepts('*test(') > 0)
assert (TokenAFDs.MT_AFD().accepts('a(e*ls)') == 0)
print("TEST TOKEN *     ->  OK")

assert (TokenAFDs.DV_AFD().accepts('/test') > 0)
assert (TokenAFDs.DV_AFD().accepts('a(/ls)') == 0)
print("TEST TOKEN /     ->  OK")

assert (TokenAFDs.NOT_AFD().accepts('!(test)') > 0)
assert (TokenAFDs.NOT_AFD().accepts('a(els)') == 0)
print("TEST TOKEN !     ->  OK")

assert (TokenAFDs.if_AFD().accepts('if(cond)') > 0)
assert (TokenAFDs.if_AFD().accepts('a(elifs)') == 0)
print("TEST TOKEN if    ->  OK")

assert (TokenAFDs.then_AFD().accepts('then EXPRESSION') > 0)
assert (TokenAFDs.then_AFD().accepts('a(elithenfs)') == 0)
print("TEST TOKEN then  ->  OK")

assert (TokenAFDs.else_AFD().accepts('else(cond)') > 0)
assert (TokenAFDs.else_AFD().accepts('a(eelse_AFDls)') == 0)
print("TEST TOKEN else  ->  OK")

assert (TokenAFDs.while_AFD().accepts('while(cond)') > 0)
assert (TokenAFDs.while_AFD().accepts('testwhiel') == 0)
print("TEST TOKEN while ->  OK")

assert (TokenAFDs.do_AFD().accepts('do EXPRESSION') > 0)
assert (TokenAFDs.do_AFD().accepts('a(edols)') == 0)
print("TEST TOKEN do    ->  OK")

assert (TokenAFDs.break_AFD().accepts('break;') > 0)
assert (TokenAFDs.break_AFD().accepts('a(els)') == 0)
print("TEST TOKEN break ->  OK")

assert (TokenAFDs.num_AFD().accepts('5268554asd') > 0)
assert (TokenAFDs.num_AFD().accepts('a54654)') == 0)
print("TEST TOKEN num   ->  OK")

assert (TokenAFDs.real_AFD().accepts('5.5655') > 2)
assert (TokenAFDs.real_AFD().accepts('555555') == 0)
print("TEST TOKEN real  ->  OK")

assert (TokenAFDs.true_AFD().accepts('true') > 0)
assert (TokenAFDs.true_AFD().accepts('false') == 0)
print("TEST TOKEN true  ->  OK")

assert (TokenAFDs.false_AFD().accepts('false') > 0)
assert (TokenAFDs.false_AFD().accepts('true') == 0)
print("TEST TOKEN false ->  OK")

assert (TokenAFDs.id_AFD().accepts('variavel92') > 0)
assert (TokenAFDs.id_AFD().accepts('(testwhiel)') == 0)
print("TEST TOKEN id    ->  OK")

assert (TokenAFDs.basic_AFD().accepts('basic') > 0)
assert (TokenAFDs.basic_AFD().accepts('a(elasdass)') == 0)
print("TEST TOKEN basic ->  OK")
