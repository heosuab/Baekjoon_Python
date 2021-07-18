total = int(input())

five = total//5
total = total%5

for i in range(0, 3):
    if total%3==0:
        three = (total//3)
        total -= three*3
        break
    if five>=1:
        five -= 1
        total += 5

print(five+three if total==0 else -1)