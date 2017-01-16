import random

N = 100000
nums = [0]

for i in range(N):
    nums.append(random.randrange(-1000,1000))

Dp = {0:0}
maximum = 0
for i in range(1, N+1):
    if Dp[i-1] + nums[i] > nums[i]:
        Dp[i] = Dp[i-1]+nums[i]
    else:
        Dp[i] = nums[i]
    if Dp[i] >= maximum:
        maximum = Dp[i]

print nums
print maximum


