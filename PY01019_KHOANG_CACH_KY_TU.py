import math
def checkKhoangCach(s):
    reversedS= s[::-1]
    for i in range(1, len(s)-1):
        if abs(ord(s[i]) - ord(s[i -1])) != abs(ord(reversedS[i]) - ord(reversedS[i-1])): return False
    return True

for _ in range(int(input())):
    s = input().strip()
    if checkKhoangCach(s): print('YES')
    else: print('NO')
        
        
        