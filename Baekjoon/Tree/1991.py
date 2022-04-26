import sys
input = sys.stdin.readline

tree = {}
for _ in range(int(input())):
    root, left, right = map(str, input().split())
    tree[root] = [left, right]
    
def before(root):
    if root != ".":
        print(root, end="")
        before(tree[root][0])
        before(tree[root][1])

def around(root):
    if root != ".":
        around(tree[root][0])
        print(root, end="")
        around(tree[root][1])

def after(root):
    if root != ".":
        after(tree[root][0])
        after(tree[root][1])
        print(root, end="")
    
before('A')
print()
around('A')
print()
after('A')