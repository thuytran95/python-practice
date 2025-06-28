def convertTo(s, s1, s2):
    return int(s.replace(s2, s1))  # Replace all occurrences of 'b' with 'a'

t = int(input())
for _ in range(t):
    a, b = input().strip().split()
    a, b = min(a, b), max(a, b)
    s1 = input()
    s2 =''

    if(len(s1.split()) >1): s1, s2 = s1.split()
    else:
        s2 = input()

    minRes = convertTo(s1, a, b) + convertTo(s2, a, b)
    maxRes = convertTo(s1, b, a) + convertTo(s2, b, a)
    print(minRes, maxRes)