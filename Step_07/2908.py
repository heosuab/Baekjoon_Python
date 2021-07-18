string_list = list(input().split())

for index, string in enumerate(string_list):
    string_list[index] = string[::-1]

print(max(map(int, string_list)))