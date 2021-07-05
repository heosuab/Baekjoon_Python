num = int(input())
line, i = 1, 1

while 1:
    if num <= line:
        break
    else:
        i += 1
        line += i

diff = line - num
if i%2==0:
    print('%d/%d'%(i-diff, 1+diff))
else:
    print('%d/%d'%(1+diff, i-diff))