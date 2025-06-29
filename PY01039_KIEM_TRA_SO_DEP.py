def kiemtra(s):
    for i in range(len(s)):
        if i % 2 == 0 and s[i] != s[0]: return False
        if i % 2 != 0 and s[i] != s[1]: return False
    return True
            
for _ in range(int(input())):
    s = input().strip()
    if kiemtra(s): print('YES')
    else: print('NO')
     
            