class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l,r,zeros,maxi = 0,0,0,0
        while r < len(nums):
            if nums[r]==0:
                zeros+=1
            if zeros>k:
                if nums[l] ==0:
                    zeros-=1
                l +=1

            if zeros<= k:
                maxi = max(maxi, r-l+1)
            r+=1
        return maxi
                
