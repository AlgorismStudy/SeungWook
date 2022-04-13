N = list(map(int, input().split()))
K = [int(input()) for _ in range(N[0])]

mid = min(K) // 2

while True:
    count = 0
    for i in K:
        count += i // mid 
    if count >= N[1]:
        mid += 1
        if count == N[1] - 1:
            print(mid-1)
            break
    else:
        mid -= 1
        if count == N[1]:
            print(mid)
            break