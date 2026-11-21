class Solution:
    def solve(self,n,dp):
        if n ==1 or n==2:
            return n
        if dp[n]!= -1:
            return dp[n]
        dp[n] =self.solve(n-1,dp) + self.solve(n-2,dp)
        return dp[n]
    def climbStairs(self, n: int) -> int:
        dp = [-1 for _ in range(n+1)]

        a =self.solve(n,dp)
        return a