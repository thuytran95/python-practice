'''
chu y: chi dem cac ky tu lien ke nhau
khong dung duoc dict
AABB121 -> 2A2B111211
'''

t = int(input())
for _ in range(t):
    s = input().strip()
    i = 0
    while i < len(s):
        cnt =1
        while i < len(s) - 1 and s[i] == s[i+1]: 
            cnt +=1
            i += 1
        print(f'{cnt}{s[i]}', end='')
        i+=1
    print()
    
    