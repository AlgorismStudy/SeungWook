import sys
input = sys.stdin.readline

n = int(input())

def check(num):
    for i in range(1, (len(num))//2 + 1):
        if num[-i:] == num[-(i*2):-i]:
            return False
    else:
        return True

def back_tracking(num):
    if len(num) == n:
        print(num)
        sys.exit()
    for i in '123':
        if check(num + i):
            back_tracking(num + i)
    return

back_tracking('1')