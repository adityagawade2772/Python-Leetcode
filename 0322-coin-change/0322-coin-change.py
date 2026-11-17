
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        def solve(rem,dp):

        
            if rem < 0:
                return float('inf')
            if dp[rem] != -1:
                return dp[rem]
            mini = float('inf')

            for coin in coins:
                
                ans = 1 + solve(rem - coin,dp)
                mini = min(mini, ans)

            dp[rem] = mini
            dp[0] =  0
            return dp[rem]
        dp = [-1 for _ in range(amount+1)]
        ans = solve(amount,dp)

        if ans == float('inf'):
            return -1

        return ans
