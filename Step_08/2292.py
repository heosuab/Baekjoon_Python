num = int(input())

i, start = 1, 1

while 1:
    if num <= start:
        break
    else:
        start += i*6
        i += 1

print(i)