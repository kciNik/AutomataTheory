from smcFile import AppClass
from genSTR import generation
import time

obj = AppClass()
ch = 1
while int(ch) != 0:
    print('1. Generate file 1000 strings')
    print('2. Write string from keyboard')
    print('3. Check file')
    print('Choose option: ')
    ch = input()
    if ch.isdigit():
        if int(ch) == 1:
            generation()
        elif int(ch) == 2:
            print('Write: ')
            s = input()
            match = obj.CheckStr(s.rstrip())
            if match:
                print(s + '  Nice string, bro')
            else:
                print('OH, NO, NOOOOOOOOOOOOO, NO, is is wrong:((')
        elif int(ch) == 3:
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
        elif int(ch) == 0:
            break
        else:
            print('Beyond choice')
    else:
        print('Not digit')
print('END')
