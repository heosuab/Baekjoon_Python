def fibonacci_count(num):
    count_zero = [1, 0]
    count_one = [0, 1]

    if num <= 1:
        return
    
    for i in range(2, num+1):
        count_zero.append(count_zero[i-1] + count_zero[i-2])
        count_one.append(count_one[i-1] + count_one[i-2])

    return count_zero, count_one

test = int(input())
count_zero, count_one = fibonacci_count(40)
for _ in range(test):
    num = int(input())
    print(count_zero[num], count_one[num])