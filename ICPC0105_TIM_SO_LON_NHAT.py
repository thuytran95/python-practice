import re
import math

t = int(input())
for _ in range(t):
    a = []
    try:
      
        a += [int(x) for x in re.split("[^0-9]", input().strip()) if x.isdigit()]
        res = max(a)
        print(res)
    except ValueError:
        print('error')