import sys
input = sys.stdin.readline
print = sys.stdout.write

sort_list = [0] * 10001
for _ in range(int(input())):
    sort_list[int(input())] += 1
            
for i in range(10001):
    for _ in range(sort_list[i]):
        print("%s\n" %i)

# for i in range(10001):
#     if sort_list[i] != 0:
#         print(f'{i}\n' * sort_list[i], end='')