def bienDoi(s):
    cntChuThuong = 0
    for c in s:
        if c >= 'a' and c <= 'z':
            cntChuThuong+=1
    if cntChuThuong < len(s) -cntChuThuong: print(s.upper())
    else: print(s.lower())

bienDoi(input().strip())