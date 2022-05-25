import sys
input = sys.stdin.readline

n, m = map(int, input().split())

result = [[i] for i in range(1, n+1)]
while m > 1:
    arr = []
    for i in result:
        for j in range(1, n+1):
            if j in i:
                continue
            else:
                arr.append(i + [j])
    result = arr
    m -= 1

for i in result:
    print(*i)