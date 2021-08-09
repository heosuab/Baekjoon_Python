brackets = []

while 1:
    brackets.clear()
    str = list(input())
    if str==['.']:
        break
    for letter in str:
        if letter in '[]()':
            brackets.append(letter)
            while len(brackets)>=2:
                if (brackets[-1]==')' and brackets[-2]=='(')or (brackets[-1]==']' and brackets[-2]=='['):
                    brackets.pop()
                    brackets.pop()
                else:
                    break
    if len(brackets)<1:
        print('yes')
    else:
        print('no')