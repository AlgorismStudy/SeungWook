X, Y = map(int,input().split())

now = (Y * 100) // X
count = 0
    
while now != 100:
    X += 1
    Y += 1
    count += 1
    next = (Y  * 100) // X
    if next > now:
        print(count)
        break
else:
    print(-1)