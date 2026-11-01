class Solution:
    def solve(self,nums,m,n,dp):
        for i in range(0,m):
            for j in range(0,n):
                if i == 0 and j ==0:
                    continue
                if nums[i][j]==1:
                    dp[i][j] =0
                    continue

                if i>0:
                    up = dp[i-1][j]
                else:
                    up = 0
                if j>0:
                    left = dp[i][j-1]
                else:
                    left = 0
                dp[i][j] = up + left
        return dp[m-1][n-1]
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _  in range(n)] for _ in range(m)]
        dp[0][0] = 1
        if obstacleGrid[0][0] ==1:
            return 0

        a = self.solve(obstacleGrid,m,n,dp)
        
        return a
        
        