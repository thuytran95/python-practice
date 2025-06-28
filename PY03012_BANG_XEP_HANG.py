if __name__ =="__main__":
    n = int(input())
    arr=[]
    for _ in range(n):
        name = input().strip()
        soBaiDung, soSubmit = map(int, input().split())
        d = {'name':name, 'soBaiDung': soBaiDung, 'soSubmit': soSubmit }
        arr.append(d)
        
    arr.sort(key = lambda x: (-x['soBaiDung'], x['soSubmit'], x['name'] ))
    for d in arr:
        s = ' '.join(map(str, d.values()))
        print(s)

