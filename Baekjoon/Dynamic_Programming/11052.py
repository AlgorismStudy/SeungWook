import sys
input = sys.stdin.readline

n = int(input())
prices = list(map(int, input().split()))

max_price = [0] * (n+1)
prices.insert(0, 0)

max_price[1] = prices[1]
for i in range(2, n+1):
    for j in range(i+1):
        if max_price[i] < prices[j] + max_price[i-j]:
            max_price[i] = prices[j] + max_price[i-j]

print(max_price[n])