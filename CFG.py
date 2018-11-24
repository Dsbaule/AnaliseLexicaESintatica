class CFG:
    def __init__(self):
        self.nonTerminals = set()
        self.terminals = set()
        self.alphabet = set()
		self.productions = dict()
		self.start_symb = ""
