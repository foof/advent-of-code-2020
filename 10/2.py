import sys

dp = dict()

def rec(nums, idx, prev):
    global dp
    key = "%d,%d" % (idx, prev)

    if key in dp:
        return dp[key]

    if nums[idx] - prev <= 3:
        if idx+1 == len(nums)-1:
            dp[key] = 1
        else:
            dp[key] = rec(nums, idx+1, nums[idx]) + rec(nums, idx+1, prev)
    else:
        dp[key] = 0

    return dp[key]

nums = [int(x) for x in open("data", "r").read().split("\n")]
nums.sort()

nums.append(nums[-1] + 3)

# for i in range(200):
#     a = []
#     for j in range(200):
#         a.append(-1)
#     dp.append(a)

ans = rec(nums, 0, 0)

total = 0
# for i in dp:
#     for j in i:
#         print(i, j)
#         if j == 1:
#             total += 1
print(dp)
print(total)


print(ans)