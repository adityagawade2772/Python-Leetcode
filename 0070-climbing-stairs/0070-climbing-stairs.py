class Solution:
    def solve(self,n,dp):
        if n ==1 or n==2:
            return n
        if dp[n]!= -1:
            return dp[n]
        dp[n] =self.solve(n-1,dp) + self.solve(n-2,dp)
        return dp[n]
    def climbStairs(self, n: int) -> int:
        if n == 1 or n==2:
            return n
        # dp = [-1 for _ in range(n+1)]
        # dp[0] =0
        # dp[1] = 1
        # dp[2] = 2
        prev2 = 1
        prev = 2
        curr = 0
        for _ in range(3,n+1):
            curr = prev+ prev2
            prev2 = prev
            prev = curr

        return curr

        return dp[n]

        # a =self.solve(n,dp)
        return a