p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
def index(x):
    return p.index(x)

while 1:
    ss = input()
    if ss[0] == '0': break # truong hop so 0 khong in ra gi ca
    else:
        k, s = ss.split()
        k = int(k)
        res = ''
        for el in s:
            res += p[(index(el) + k) % 28] # cong tong index cua el trong p + k chia du 28
        print(res[::-1])