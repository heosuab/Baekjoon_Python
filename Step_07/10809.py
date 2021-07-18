# [a-z(26개)] 아스키코드 'a':97, 'z':122

is_list = [-1 for i in range(97, 123)]
str_list = list(map(ord, str(input())))

for index, ascii in enumerate(str_list):
    if is_list[ascii-97] == -1:
        is_list[ascii-97] = index

print(*is_list)