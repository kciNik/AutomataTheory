from checkREG import check
from checkREG import checkrstr
from genSTR import generation

ch = 1
use = {}
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
            use = checkrstr(s, use)
        elif int(ch) == 3:
            use = check(use)
        elif int(ch) == 0:
            break
        else:
            print('Beyond choice')
    else:
        print('Not digit')
print('END')
