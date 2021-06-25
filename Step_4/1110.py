num = input()

if len(num)==1:
    num = "0"+num[0]
initial = num

count = 0

while True:
    sum = str(int(num[0])+int(num[1]))
    if len(sum)==1:
        sum = "0"+sum[0]

    num = num[1]+sum[1]
    count += 1
    
    if(num==initial):
        print(count)
        break
