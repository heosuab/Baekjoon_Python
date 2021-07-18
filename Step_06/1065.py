def hans(n):
    num_list = list(map(int, str(n)))
    if (num_list[1]-num_list[0])!=(num_list[2]-num_list[1]):
        return False
    return True

if __name__ == "__main__":
    num = int(input())
    hans_count = 0    

    for i in range(1, num+1):
        if i<100:
            hans_count += 1
        elif hans(i):
            hans_count += 1

    print(hans_count)