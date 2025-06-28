def kiemTraMayMan(s):
    for c in s:
        if c != '4' and c != '7': return False
    return True

t = int(input())
for _ in range (t):
    s = input().strip()
    if kiemTraMayMan(s): print('YES')
    else: print('NO')