repeat = int(input())

for i in range(0, repeat):
    length, string = input().split()
    output = ""
    for i in range(0, len(string)):
        output += string[i]*int(length)
    print(output)