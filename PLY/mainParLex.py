from Parcer import Pars
from genSTR import generation
import time

parser = Pars()
menu = 1
while int(menu) != 0:
    print('1. Generate and check file')
    print('2. Write string from keyboard')
    print('Choose option: ')
    menu = input()
    if menu.isdigit():
        if int(menu) == 1:
            generation()
            f = open('genSTR.txt', 'r')
            start = time.time()
            for line in f:
                parser.CheckStr(line.rstrip())
            end = time.time()
            parser.putInFile()
            print('Flex time: ', end - start)
            f.close()
        elif int(menu) == 2:
            print('Write: ')
            s = input()
            r = parser.CheckStr(s)
            if parser.flag:
                print(s, end=' ')
                print('Nice string, bro')
            else:
                print('no, no, no')
        elif int(menu) == 0:
            break
        else:
            print('Beyond choice')
    else:
        print('Not digit')
print('END')
