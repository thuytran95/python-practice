t = int(input())
for _ in range(t):
    s = input().strip() 
    res = ''  
    for i in range(0, len(s) -1, 2):
        res += s[i] * (int(s[i + 1]))
    print(res)