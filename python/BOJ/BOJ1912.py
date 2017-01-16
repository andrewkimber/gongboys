N = int(raw_input())
nums = [-1001]

nums += map(int, raw_input().split())


Dp = {}
# the choice of NOT CHOOSING is included by this phrase Dp[1] = 0
if nums[1] < 0:
    Dp[1] = 0
else:
    Dp[1] = nums[1]
maximum = Dp[1]
for i in range(2, N+1):
    if Dp[i-1] + nums[i] > nums[i]:
        Dp[i] = Dp[i-1]+nums[i]
    else:
        Dp[i] = nums[i]
    if Dp[i] >= maximum:
        maximum = Dp[i]


# in case nothing is chosen!!! you have to add AT LEAST one!
if maximum == 0:
    maximum = max(nums)

print maximum


