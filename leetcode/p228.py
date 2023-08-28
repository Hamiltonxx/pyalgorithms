nums = [0,1,2,4,5,7]

n = len(nums)
# if n == 0: return [""]
ans = [[nums[0]]]
print(ans)
for x in nums[1:]:
    if x == ans[-1][-1] + 1:
        ans[-1].append(x)
    else:
        ans.append([x])
print(['->'.join(str(x)) for x in ans])