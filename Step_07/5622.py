dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

phone_number = list(input())
count = 0

for num in phone_number:
    for index, value in enumerate(dial):
        if num in value:
            count += (index+3)

print(count)