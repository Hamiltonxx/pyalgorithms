import bisect
def lis(nums):
    piles = []
    for num in nums:
        pile = bisect.bisect_left(piles,num)
        if pile == len(piles):
            piles.append(num)
        else:
            piles[pile] = num 
    return len(piles)

nums = [10,9,2,5,3,7,101,18]
# nums = [0,1,0,3,2,3]
# nums = [7,7,7,7,7,7,7]

print(lis(nums))