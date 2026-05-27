import re

class Token:
    def __init__(self, type_, value, line):
        self.type = type_
        self.value = value
        self.line = line

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)}, line={self.line})"

class Lexer:
    TOKEN_SPEC = [
        ('RULE',      r'\brule\b'),
        ('IF',        r'\bif\b'),
        ('THEN',      r'\bthen\b'),
        ('AND',       r'\bAND\b'),
        ('COLON',     r':'),
        ('ASSIGN',    r'='),
        ('RELOP',     r'[><=]'),
        ('VALUE',     r'\d+'),
        ('ID',        r'[a-z][a-z0-9_]*'),
        ('NEWLINE',   r'\n'),
        ('SKIP',      r'[ \t\r]+'),
        ('MISMATCH',  r'.'),
    ]

    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self._tokenize()

    def _tokenize(self):
        regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.TOKEN_SPEC)
        line_num = 1
        
        for mo in re.finditer(regex, self.source_code):
            kind = mo.lastgroup
            value = mo.group(kind)
            
            if kind == 'NEWLINE':
                line_num += 1
                continue
            elif kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise SyntaxError(f"Error Léxico: Carácter ilegal {repr(value)} en la línea {line_num}")
            
            # Ajuste semántico por si un '=' cae bajo RELOP o ASSIGN según el contexto del Parser
            self.tokens.append(Token(kind, value, line_num))