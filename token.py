from enum import Enum

class TokenKind(Enum):
    # Operators
    PLUS     = 0
    MINUS    = 1
    ASTERISK = 3
    SLASH    = 4
    
    
    NUMBER   = 5
    IDENT    = 6
    
    # Keywords
    VOID     = 7
    INT      = 8

class Token:
    def __init__(self, kind, value=None):
        self.kind = kind
        self.value = value
