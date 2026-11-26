class Solution:
    def solve(self, i, j,triangle,dp):
        if i == len(triangle) - 1:
            return triangle[i][j]
        if dp[i][j] != -1:
            return dp[i][j]

        down= triangle[i][j] + self.solve(i+1,j,triangle,dp)
        digonal = triangle[i][j]  + self.solve(i+1,j+1,triangle,dp)
        dp[i][j] = min(down,digonal)
        return dp[i][j]
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = [[-1 for _ in range(len(triangle))]for _ in range(len(triangle))]
        n = len(triangle)
        dp[0][0]= triangle[0][0]
        for i in range(0,n):
            dp[n-1][i] = triangle[n-1][i]

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                down = triangle[i][j] +dp[i+1][j]
                digonal= triangle[i][j] +dp[i+1][j+1]
                dp [i][j] = min(down,digonal)
        # a = self.solve(0,0,triangle,dp)

        return dp[0][0]
        