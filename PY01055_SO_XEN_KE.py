def checkValid(s):
    if len(s) % 2 == 0 or len(s) < 3: return False
    if s[0] == s[1]: return False
    
    for i in range(2, len(s), 2):
        if s[0] != s[i]: return False
    return True
        
for _ in range(int(input())):
    s = input().strip()
    if checkValid(s): print('YES')
    else: print('NO')