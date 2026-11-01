class Solution:
    def solve(self, m,n, grid, dp):
        if m==0 and n==0:
            return grid[m][n]
        if dp[m][n] != 0:
            return dp[m][n]
        if m > 0 :
            up = self.solve(m-1,n,grid,dp)
        else:
            up = float("inf")
        if n > 0:
            left= self.solve(m,n-1,grid,dp)
        else:
            left = float("inf")
        dp[m][n] = grid[m][n] +  min(up,left)
        return dp[m][n]

    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)]for _ in range(m)]
        a = self.solve(m-1,n-1,grid, dp)
        return a
        