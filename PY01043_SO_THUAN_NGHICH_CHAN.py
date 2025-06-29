'''
so thuan nghich nho nhat tinh la 22
'''
def checkValid(s):
    if(len(s) % 2 != 0 or s != s[::-1]): return False
    for el in s:
        if int(el) % 2 != 0: return False
    return True

for _ in range(int(input())):
    n = int(input().strip())
    for i in range(22 ,n , 2): #vi la so chan buoc nhay la 2, giam thieu thoi gian lap
        if checkValid(str(i)): print(i, end=' ')
    print()