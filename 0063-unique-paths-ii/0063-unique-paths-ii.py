class Solution:
    def solve(self,nums,m,n,dp):
        prev= [0]*n
        for i in range(0,m):
            cur =[0] *n
            for j in range(0,n):
                if i == 0 and j ==0:
                    cur[j] = 1
                    continue
                if nums[i][j]==1:
                    cur[j] =0
                    continue

                if i>0:
                    up = prev[j]
                else:
                    up = 0
                if j>0:
                    left = cur[j-1]
                else:
                    left = 0
                cur[j] = up + left
            prev = cur

        return prev[n-1]
        
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _  in range(n)] for _ in range(m)]
        dp[0][0] = 1
        if obstacleGrid[0][0] ==1:
            return 0

        a = self.solve(obstacleGrid,m,n,dp)
        
        return a
        
        