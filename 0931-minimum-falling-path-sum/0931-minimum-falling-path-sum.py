class Solution:
    def  solve(self,i,j,c,nums, dp ):
        
        if j<0 or j>=c:
            return float("inf")
        if i == 0:
            return nums[0][j]
        if dp[i][j] != 200:
            return dp[i][j]

        up = nums[i][j] + self.solve(i-1, j,c,nums,dp)
        left= nums[i][j] + self.solve(i-1,j-1,c,nums,dp)
        right = nums[i][j] + self.solve(i-1, j+1,c, nums,dp)
        dp[i][j] = min(up, left, right)
        return dp[i][j]
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        c = len(matrix[0])
        dp = [[200 for _ in range(c)] for _ in range(c)]
        mini = float("inf")
        for i in range(c):
            mini = min(mini, self.solve(c-1,i,c,matrix, dp))
        return mini

