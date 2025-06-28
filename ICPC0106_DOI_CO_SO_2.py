binary_8 = {
    "000": 0,
    "001": 1,
    "010": 2,
    "011": 3,
    "100": 4,
    "101": 5,
    "110": 6,
    "111": 7
}
binary_4= {
    "00": 0,
    "01": 1,
    "10": 2,
    "11": 3
}
binary_16 = {
    "0000": 0,
    "0001": 1,
    "0010": 2,
    "0011": 3,
    "0100": 4,
    "0101": 5,
    "0110": 6,
    "0111": 7,
    "1000": 8,
    "1001": 9,
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F"
}

def convert_binary (binaryList, n):
    res = []
    if n == 4:
        for el in binaryList:
            res.append(binary_4.get(el))
    elif n == 8:
        for el in binaryList:
            res.append(binary_8.get(el))
    else:
        for el in binaryList:
            res.append(binary_16.get(el))
    print(''.join(map(str, res)))

def splitGroupBinary(s, n):
    res = [s[i: i + n] for i in range(0, lenStr, n)]
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    lenStr = len(s)
    d = 0
    if n == 2:
        print(s)
    else:
        if n == 4:
            if lenStr % 2 != 0:
                d = 2 - lenStr % 2
        elif n == 8:
            if lenStr % 3 != 0:
                d = 3 - lenStr % 3
        elif n == 16:
            if lenStr % 4 != 0:
                d = 4 - lenStr % 4 
        s = '0' * d + s          
        res = []
        if n == 4:
            res = splitGroupBinary(s, 2)
        elif n  == 8:
            res = splitGroupBinary(s, 3)
        else:
            res = splitGroupBinary(s, 4)
        convert_binary(res, n)
            
            
    
      
            
            