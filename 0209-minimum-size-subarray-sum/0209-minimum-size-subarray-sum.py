class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 0
        count = float("inf")
        i = 0
        for r in range(len(nums)):
            res += nums[r]
            
            while res >= target:
                count = min(count, r-i+1)
                res -= nums[i]
                i +=1

        return 0 if count == float("inf") else count
            


        