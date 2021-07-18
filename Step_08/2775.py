num = int(input())

for i in range(0, num):
    floor = int(input())
    next = int(input())
    
    people = [i+1 for i in range(0, next)]

    for i in range(1, floor+1):
        for j in range(1, next):
            people[j] += people[j-1]

    print(people[next-1])