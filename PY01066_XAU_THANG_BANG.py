def checkValid(s):
    if len(s) < 2: return False
    s1 = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s1[i]) - ord(s1[i- 1])): return False
    return True

for _ in range(int(input())):
    s = input().strip()
    if checkValid(s): print('YES')
    else: print('NO')