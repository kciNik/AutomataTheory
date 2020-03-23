import re
import ply.lex as lex


class Lexer:
    states = (('name', 'exclusive'),
              ('size', 'exclusive'),
              ('hash', 'exclusive'),
              ('tail', 'exclusive'))
    tokens = ('ED2K', 'NAME', 'SIZE', 'HASH', 'NEWLINE', 'TAIL', 'UNKNOWN')

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def input(self, data):
        return self.lexer.input(data)

    def token(self):
        return self.lexer.token()

    def t_ED2K(self, t):
        r'^(?m)ed2k://'
        if t.lexer.current_state() == 'INITIAL':
            t.lexer.begin('name')
        else:
            t.lexer.begin('INITIAL')
        return t

    def t_NEWLINE(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_UNKNOWN(self, t):
        r'.+'
        return t

    def t_name_NAME(self, t):
        r'\|file\|([a-zA-Z\+\-\_\.]{1,})\|'
        t.lexer.begin('size')
        return t

    def t_name_NEWLINE(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_name_UNKNOWN(self, t):
        r'.+'
        t.lexer.begin('INITIAL')
        return t

    def t_size_SIZE(self, t):
        r'([0-9]{1,})\|'
        t.lexer.begin('hash')
        return t

    def t_size_NEWLINE(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_size_UNKNOWN(self, t):
        r'.+'
        t.lexer.begin('INITIAL')
        return t

    def t_hash_HASH(self, t):
        r'([a-fA-F0-9]{32})'
        t.lexer.begin('tail')
        return t

    def t_hash_NEWLINE(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_hash_UNKNOWN(self, t):
        r'.+'
        t.lexer.begin('INITIAL')
        return t

    def t_tail_TAIL(self, t):
        r'\|/'
        t.lexer.begin('INITIAL')
        return t

    def t_tail_NEWLINE(self, t):
        r'(\n)'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        return t

    def t_tail_UNKNOWN(self, t):
        r'.+'
        t.lexer.begin('INITIAL')
        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_name_error(self, t):
        print("Illegal character in name '%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_size_error(self, t):
        print("Illegal character in size'%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_hash_error(self, t):
        print("Illegal character in hash'%s'" % t.value[0])
        t.lexer.begin('INITIAL')

    def t_tail_error(self, t):
        print("Illegal character in tail'%s'" % t.value[0])
        t.lexer.begin('INITIAL')

