import json

f = open("onthi/flights.json")
data = json.load(f)
flights = data['flights']

for _ in range(int(input())):
    x, y = map(int, input().split())
    tong = 0
    ok = False
    for item in flights:
        year  = int(item['year'])
        if year >= x and year <y:
            tong += int(item['passengers'])
            ok = True
    if ok:
        print(tong)
    else:
        print('Invalid')