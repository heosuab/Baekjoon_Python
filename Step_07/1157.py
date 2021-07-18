list_string = list(input().upper())
max = ''
overlap = False

for cur in set(list_string):
    if list_string.count(cur) >= list_string.count(max):
        if (list_string.count(cur) == list_string.count(max)) and cur != max:
            overlap = True
        else:
            max = cur
            overlap = False

if overlap:
    print("?")
else:
    print(max)