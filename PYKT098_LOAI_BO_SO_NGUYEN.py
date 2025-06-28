import re

with open('DATA.in', 'r') as file:
    ans = []
    for dong in file:
        for el in dong.split():
            try:
                x= int(el)
                # dich so 1 sang trai 63 bit, tuong ung voi 1 * 2^63
                if x > (1<< 63): ans.append(el)
            except ValueError:
                ans.append(el)
    
    ans.sort()
    print(' '.join(ans))
        
    