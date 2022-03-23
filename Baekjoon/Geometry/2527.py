import sys
input = sys.stdin.readline

for i in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    
    result = 'a'
    if x2 < x3 or y2 < y3 or y4 < y1 or x4 < x1:
        result = 'd'
    if x2 == x3:
        if y1 == y4 or y2 == y3: result = 'c'
        else: result = 'b'
    if y2 == y3:
        if x1 == x4 or x2 == x3: result = 'c'
        else: result = 'b'
    if x1 == x4:
        if y1 == y4 or y2 == y3: result = 'c'
        else: result = 'b'
    if y1 == y4:
        if x1 == x4 or x2 == x3: result = 'c'
        else: result = 'b'
        
    print(result)