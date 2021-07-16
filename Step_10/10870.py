def fivo(num):
    if num<=1:
        return num
    return fivo(num-2)+fivo(num-1)


num = int(input())
print(fivo(num))