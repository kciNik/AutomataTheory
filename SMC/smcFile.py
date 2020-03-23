import smcFile_sm
import time


class AppClass:
    def __init__(self):
        self._fsm = smcFile_sm.AppClass_sm(self)
        self._fsm.enterStartState()
        self._is_acceptable = False
        self._length = 0
        self._count = 0
        self._name = ''
        self._dict = {}
        self._c = ''

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

    def count(self):
        self._count += 1

    def isCount1(self):
        return self._count == 1

    def isCount2(self):
        return self._count == 2

    def isCount3(self):
        return self._count == 3

    def isCount4(self):
        return self._count == 4

    def isCount5(self):
        return self._count == 5

    @staticmethod
    def printerr():
        print('Error')

    def isLess4(self):
        return self._length < 4

    def isLess2(self):
        return self._length < 2

    def isLess32(self):
        return self._length < 31

    def CheckStr(self, string):
        self._fsm.Start()
        string = string.lower()
        for c in string:
            self._c = c
            if c.isalpha():
                if 'a' <= c <= 'f':
                    self._fsm.AFLetter()
                else:
                    self._fsm.Letter()
            elif c.isdigit():
                self._fsm.Digit()
            elif c == '|':
                self._fsm.VertSym()
            elif c == '+' or c == '-' or c == '_' or c == '.':
                self._fsm.SymbolSym()
            elif c == '/':
                self._fsm.SlashSym()
            elif c == ':':
                self._fsm.ColonSym()
            elif c == ' ':
                self._fsm.SpaceSym()
            elif c == '\n':
                self._fsm.EOS()
                break
            else:
                self._fsm.Unknown()
        self._fsm.EOS()
        return self._is_acceptable

    def LengthInc(self):
        self._length += 1

    def LengthZero(self):
        self._length = 0

    def isED2K(self):
        t = (self._name == "ed2k")
        self._name = ''
        return t

    def isFile(self):
        t = (self._name == "file")
        self._name = ''
        return t

    def ClearSMC(self):
        self.LengthZero()
        self._name = ''
        self._count = 0
        self._is_acceptable = True

    def LengthNoZero(self):
        return self._length > 0

    def PutInDec(self):
        if self._dict.get(self._name) is None:
            self._dict[self._name] = 1
        else:
            self._dict[self._name] += 1

    def makeName(self):
        self._name += self._c

    @property
    def dict(self):
        return self._dict


obj = AppClass()
f = open('genSTR.txt', 'r')
res = open('rightSTR.txt', 'w')
start = time.time()
for line in f.readlines():
    match = obj.CheckStr(line.rstrip())
end = time.time()
print(end - start)
for key in obj.dict.keys():
    res.write(key + ' ')
    res.write(str(obj.dict[key]) + '\n')
res.close()
f.close()
