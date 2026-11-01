class Solution:
    def solve(self,n,nums, dp ):
        for i in range(1,n):
            if i ==1:
                pick = nums[i]
            else:
                pick = nums[i] + dp[i-2]
            not_pick = dp[i-1]
            dp[i] = max(pick, not_pick)
        return dp[n-1]
        
        

    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]
        dp[0]= nums[0]
        a = self.solve(n, nums, dp)
        return a

