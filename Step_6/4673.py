def d(n):
    sum = n
    num = str(n)
    for i in range(0, len(num)):
        sum += int(num[i])
    return sum

if __name__ == "__main__":
    num_list = [i for i in range(1, 10001)]
    for i in range(1, 10001):
        if d(i) in num_list:
            num_list.remove(d(i))
    for i in num_list:
        print(i) 