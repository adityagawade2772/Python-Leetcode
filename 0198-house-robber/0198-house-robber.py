class Solution:
    def solve(self,index,nums, dp ):
        if index<0:
            return 0
        if index==0:
            return nums[0]
        if dp[index]!=-1:
            return dp[index]
        pick = nums[index]+ self.solve(index-2,nums,dp)
        not_pick = self.solve(index-1,nums,dp)
        dp[index] = max(pick, not_pick)
        return dp[index]

    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]
        a = self.solve(n-1, nums, dp)
        return a

