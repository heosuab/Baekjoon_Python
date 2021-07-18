x = int(input())
y = int(input())

area = 0

if x>0:
    area=1 if y>0 else 4
else:
    area=2 if y>0 else 3

print(area)
