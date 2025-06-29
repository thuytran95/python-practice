import itertools

n, k = map(int, input().split())
# chu y bai toan to hop so phai convert ve in 
# neu de str se bi sai
a = list(set(map(int, input().split()))) 
a.sort()

for toHop in itertools.combinations(a, k):
    print(' '.join(map(str, toHop)))

