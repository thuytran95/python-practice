s = input().strip()
cnt_4, cnt7 = s.count('4'), s.count('7')
cnt = cnt_4 + cnt7
if cnt == 4 or cnt == 7: print('YES')
else: print('NO')