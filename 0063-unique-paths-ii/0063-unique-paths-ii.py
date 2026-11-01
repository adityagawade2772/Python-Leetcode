class Solution:
    def solve(self,nums,m,n,dp):

        if m == 0 and n ==0:
            if nums[m][n] == 1:
                return 0

            return 1
        if m < 0 or n< 0:
            return 0
        if nums[m][n] == 1:
            return 0

        if dp[m][n] != -1:
            return dp[m][n]

        up = self.solve(nums,m-1,n,dp)
        left = self.solve(nums,m,n-1,dp)
        dp[m][n] = up + left
        return dp[m][n]
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _  in range(n)] for _ in range(m)]
        a = self.solve(obstacleGrid,m-1,n-1,dp)
        return a
        
        