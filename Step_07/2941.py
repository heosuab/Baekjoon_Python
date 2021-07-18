char_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = input()

for al in char_list:
    string = string.replace(al, 'a')

print(len(string))