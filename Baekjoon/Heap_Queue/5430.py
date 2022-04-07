import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    play = list(input())
    n = int(input())
    arr = input().rstrip().replace('[','').replace(']', '').split(',')
    arr = deque(arr)
    
    rev = 0
    flag = 0
    for i in play:
        if i == 'R':
            rev += 1
        elif i == 'D':
            if len(arr) == 0 or arr == deque(['']):
                print('error')
                flag = 1
                break
            else:
                if rev % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    
    if flag == 0:
        if rev % 2 == 1:
            arr.reverse()
        print('['+','.join(arr)+']')