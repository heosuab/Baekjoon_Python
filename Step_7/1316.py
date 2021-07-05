num = int(input())
is_group = [True for i in range(0, num)]

for i in range(0, num):
    string = input()
    for index, char in enumerate(string):
        while (index != len(string)-1) and (char == string[index+1]):
            index += 1
        if char in string[index+1:]:
            is_group[i] = False

print(is_group.count(True))