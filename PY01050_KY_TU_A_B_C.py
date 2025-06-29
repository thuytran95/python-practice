from itertools import product


def checkHopLe(s):
    cntA = s.count('A')
    cntB = s.count('B')
    cntC = s.count('C')
    return 0 < cntA <= cntB <= cntC

n = int(input())
res = []
for i in range(3, n + 1):
    # su dung product de sinh to hop lap
    # da theo thu tu tu dien => khong can sort
    for el in product('ABC', repeat=i): 
        s =''.join(el)
        if checkHopLe(s): res.append(s)

for el in res:
    print(el)