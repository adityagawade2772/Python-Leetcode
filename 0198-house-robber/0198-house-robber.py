class Solution:
    def solve(self,nums,dp,n):
        prev = nums[0]
        prev2 = float("-inf")

        for index in range(1,n):
            
            
            if index > 1:
                pick = nums[index]+ prev2
            else: 
                pick =nums[index]
            not_pick = 0 + prev
            curr = max(pick, not_pick)
            prev2 = prev
            prev = curr
            
        return prev



    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]
        a = self.solve(nums, dp, n)
        return a

