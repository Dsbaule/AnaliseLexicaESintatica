from AFD import AFD
from AFND import AFND
import TokenAFDs

OP_AFD = TokenAFDs.OP_AFD()
CP_AFD = TokenAFDs.CP_AFD()
OPCP_AFND = AFND([OP_AFD, CP_AFD])

print(str(OP_AFD))
print()
print(str(CP_AFD))
print()
print(str(OPCP_AFND))
print()
print()
print('Testing Accepting:')
print(str(OPCP_AFND.accepts('()')))
