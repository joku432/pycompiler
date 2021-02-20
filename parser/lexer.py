import ctoken

class Lexer:
    def __init__(self, filename):
        self.filename = filename
        self.tokens   = []
        self.count    = 0

    def lex(self):
        with open(self.filaname, "r") as f:
            for line in f:
                for c in line:
                    if c.isalpha():
                        self._make_ident()
                    elif c.isdigit():
                        self._make_number()
                        
    def _make_ident(self):
        pass

    def _make_number(self):
        pass        

     
        