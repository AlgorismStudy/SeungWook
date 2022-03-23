import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    
    if x1 == x2 and y1 == y2:
        if r1 == r2: print(-1)
        else: print(0)
    else:
        R, r = max(r1, r2), min(r1, r2)
        if dis + r < R or dis > r + R:
            print(0)
        elif dis + r == R or dis == r + R:
            print(1)
        else:
            print(2)
        
        
        
        
    