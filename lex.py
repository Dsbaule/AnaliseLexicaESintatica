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

        self.input = ""
        self.length = 0
        self.index = 0
        self.table = dict()
        self.tokens = list()

        self.buffersize = 256
        self.syncTokens = ['\n','\t',' ','{','}','[',']','(',')',';']

    def setInput(self, string):
        self.input = string
        self.length = len(self.input)
        self.index = 0
        self.table.clear()
        self.tokens.clear()

    def getSymbolTable(self):
        return self.table

    def getCleanSymbolTable(self):
        cleanTable = self.table.copy()
        for lexeme, token in self.table.items():
            if token in ['ws','tb','nl','Error']:
                cleanTable.pop(lexeme, None)
        return cleanTable

    def getTokens(self):
        return self.tokens

    def getCleanTokens(self):
        return [token for token in self.tokens if token not in ['ws','tb','nl','Error']]


    def generateAllTokens(self):
        while(self.index < self.length):
            (length, token) = self.getNextToken(False)
            if length is 0:
                self.panicRecovery()

    def panicRecovery(self):
        while self.index < self.length:
            if self.input[self.index] in self.syncTokens:
                break
            self.index += 1

    def getNextToken(self, clean = True):
        while self.index < len(self.input):
            longesttoken = 0
            token = 'Error'

            string = self.input[self.index:(self.index + self.buffersize)]

            tokensize = self.OP_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.OP_AFD.getTokenName()
            tokensize = self.CP_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.CP_AFD.getTokenName()
            tokensize = self.OB_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.OB_AFD.getTokenName()
            tokensize = self.CB_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.CB_AFD.getTokenName()
            tokensize = self.OCB_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.OCB_AFD.getTokenName()
            tokensize = self.CCB_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.CCB_AFD.getTokenName()
            tokensize = self.SC_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.SC_AFD.getTokenName()
            tokensize = self.OR_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.OR_AFD.getTokenName()
            tokensize = self.AND_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.AND_AFD.getTokenName()
            tokensize = self.EQ_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.EQ_AFD.getTokenName()
            tokensize = self.NEQ_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.NEQ_AFD.getTokenName()
            tokensize = self.LT_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.LT_AFD.getTokenName()
            tokensize = self.LE_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.LE_AFD.getTokenName()
            tokensize = self.GE_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.GE_AFD.getTokenName()
            tokensize = self.GT_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.GT_AFD.getTokenName()
            tokensize = self.ATT_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.ATT_AFD.getTokenName()
            tokensize = self.PL_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.PL_AFD.getTokenName()
            tokensize = self.MN_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.MN_AFD.getTokenName()
            tokensize = self.MT_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.MT_AFD.getTokenName()
            tokensize = self.DV_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.DV_AFD.getTokenName()
            tokensize = self.NOT_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.NOT_AFD.getTokenName()
            tokensize = self.if_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.if_AFD.getTokenName()
            tokensize = self.then_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.then_AFD.getTokenName()
            tokensize = self.else_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.else_AFD.getTokenName()
            tokensize = self.while_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.while_AFD.getTokenName()
            tokensize = self.do_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.do_AFD.getTokenName()
            tokensize = self.break_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.break_AFD.getTokenName()
            tokensize = self.num_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.num_AFD.getTokenName()
            tokensize = self.real_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.real_AFD.getTokenName()
            tokensize = self.true_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.true_AFD.getTokenName()
            tokensize = self.false_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.false_AFD.getTokenName()
            tokensize = self.basic_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.basic_AFD.getTokenName()
            tokensize = self.id_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.id_AFD.getTokenName()
            tokensize = self.nl_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.nl_AFD.getTokenName()
            tokensize = self.ws_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.ws_AFD.getTokenName()
            tokensize = self.tb_AFD.accepts(string)
            if tokensize > longesttoken:
                longesttoken = tokensize
                token = self.tb_AFD.getTokenName()

            self.table[string[:longesttoken]] = token
            self.tokens.append(token)
            self.index += longesttoken
            if clean:
                if token in ['ws','tb']:
                    continue
            return (longesttoken, token)
        return (1, '$')
