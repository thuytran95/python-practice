import re

if __name__ == "__main__":
    s = ''
    while True:
        try:
            s += input()
        except EOFError:
            break
    lines = re.split(r'[.!?]', s)

    for line in lines:
        tmp = ' '.join(line.split())
        if any(c.isalnum() for c in tmp):
            tmp = tmp[0].upper() + tmp[1:].lower() if tmp else ''
            print(tmp)


        