s = input()
if len(s) <= 3: print(s)
else:
    s1 = s[::-1]
    s1 =','.join(s1[i: i + 3] for i in range(0, len(s1), 3))
    s1 = s1[::-1]
    print(s1)
