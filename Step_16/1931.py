conf = int(input())
conf_list = []
conf_count = 0
conf_time = 0

for _ in range(conf):
    start, end = map(int, input().split())
    conf_list.append([start, end])

conf_list = sorted(conf_list, key = lambda time: time[0])
conf_list = sorted(conf_list, key = lambda time: time[1])

for i in conf_list:
    if conf_time <= i[0]:
        conf_time = i[1]
        conf_count += 1

print(conf_count)