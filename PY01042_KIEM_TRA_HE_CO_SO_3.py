coSo = '012'

def kiemtraCoSo3(s):
    for el in s:
        if el not in coSo: return False
    return True

for _ in range(int(input())):
    s = input().strip()    
    if kiemtraCoSo3(s): print('YES')
    else: print('NO')