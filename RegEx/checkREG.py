import re
import time

right = '^ed2k://\\|file\\|([a-zA-Z\\+\\-\\_\\.]{1,})\\|([0-9]{1,})\\|(?P<hash>[0-9a-fA-F]{32})\\|/'


def check(use):
    f = open('genSTR.txt', 'r')
    res = open('rightSTR.txt', 'w')
    start = time.time()
    for line in f.readlines():
        match = re.fullmatch(right, line.rstrip())
        if match:
            if use.get(match.group('hash')):
                use[match.group('hash')] += 1
            else:
                use[match.group('hash')] = 1
    end = time.time()
    for key in use.keys():
        res.write(key + ' ')
        res.write(str(use[key]) + '\n')
    print(end - start)
    f.close()
    res.close()
    return use


def checkrstr(line, use):
    match = re.fullmatch(right, line.rstrip())
    if match:
        if use.get(match.group('hash')):
            print(match.group('hash'), end=' ')
            use[match.group('hash')] += 1
            print(use[match.group('hash')])
        else:
            use[match.group('hash')] = 1
            print(match.group('hash'), end=' ')
            print(use[match.group('hash')])
    else:
        print('Unacceptable')
    return use
