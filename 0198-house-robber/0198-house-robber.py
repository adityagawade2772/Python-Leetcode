class Solution:
    def solve(self, index,nums,dp):
        if index==0:
            return nums[index]
        if index<0:
            return 0
        if dp[index]!= -1:
            return dp[index]
        pick= nums[index]+ self.solve(index-2,nums,dp)
        notpick=self.solve(index-1,nums,dp)
        dp[index]= max(pick, notpick)
        return dp[index]
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n)]
        dp[0]=nums[0]
        a = self.solve(n-1,nums,dp)
        return  dp[n-1]
        