from ClassLex import Lexer
import ply.yacc as yacc
import sys


class Pars:
    tokens = Lexer.tokens

    def __init__(self):
        self._lexer = Lexer()
        self._parser = yacc.yacc(module=self, optimize=1, debug=False, write_tables=False)
        self._a = dict()
        self.resfile = open('ResParc.txt', 'w')
        self.flag = False

    def CheckStr(self, string):
        self.flag = False
        res = self._parser.parse(string)
        return res

    def p_address(self, p):
        """address : ED2K NAME SIZE HASH TAIL"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        self.flag = True
        if self._a.get(p[4]) is None:
            self._a[p[4]] = 1
        else:
            self._a[p[4]] += 1

    def p_address_zero_err_type(self, p):
        """address : err NEWLINE"""
        p[0] = p[1] + p[2]

    def p_address_third_err_type(self, p):
        """address : ED2K err NEWLINE"""
        p[0] = p[1] + p[2] + p[3]

    def p_address_first_err_type(self, p):
        """address : ED2K NAME err NEWLINE"""
        p[0] = p[1] + p[2] + p[3] + p[4]

    def p_address_second_err_type(self, p):
        """address : ED2K NAME SIZE err NEWLINE"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

    def p_address_forth_err_type(self, p):
        """address : ED2K NAME SIZE HASH err NEWLINE"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

    def p_address_fivth_err_type(self, p):
        """address : ED2K NAME SIZE HASH TAIL err NEWLINE"""
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]

    def p_err(self, p):
        """err : UNKNOWN """
        p[0] = p[1]

    def p_error(self, p):
        print('Unexpected token', p)

    def putInFile(self):
        for key in self._a.keys():
            self.resfile.write(key + ' ')
            self.resfile.write(str(self._a[key]) + '\n')
