import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

result = 0
while n != 0:    
    if r >= 2**(n-1) and c >= 2**(n-1):
        result += 2**(n-1) * 2**(n-1) * 3
        r -= 2**(n-1)
        c -= 2**(n-1)
    
    elif r >= 2**(n-1) and c < 2**(n-1):
        result += 2**(n-1) * 2**(n-1) * 2
        r -= 2**(n-1)
        
    elif r < 2**(n-1) and c >= 2**(n-1):
        result += 2**(n-1) * 2**(n-1) * 1
        c -= 2**(n-1)
    
    else:
        result += 2**(n-1) * 2**(n-1) * 0
        
    n -= 1

print(result)