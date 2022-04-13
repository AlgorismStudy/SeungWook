import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
count = 0
for i in range(n):
    temp = nums[:i] + nums[i+1:]
    start = 0
    end  = n - 2

    while start < end:
        result = temp[start] + temp[end]
        if result == nums[i]:
            count += 1
            break
        elif result > nums[i]:
            end -= 1
        else:
            start += 1

print(count)