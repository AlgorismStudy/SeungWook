import sys

input = sys.stdin.readline

N = int(input())
N_list = sorted(list(map(int, input().split())))

M = int(input())
M_list = list(map(int, input().split()))

array = [0] * 123456789
for i in N_list:
    array[int(i)] = 1

for i in M_list:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')