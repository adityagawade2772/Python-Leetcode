class Solution:
    def recur(self,i,j1,j2,matrix,r,c,dp):
        if j1<0 or j1>=c or j2<0 or j2>=c:
            return float("-inf")
        if i == r-1:
            if j1==j2:
                return matrix[i][j1]
            return matrix[i][j1] + matrix[i][j2]

        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]

        maxi = 0
        for new_j1 in range(-1,2):
            for new_j2 in range(-1,2):
                if j1 == j2:
                    ans =matrix[i][j1] + self.recur(i+1, j1 + new_j1, j2 + new_j2,matrix,r,c,dp)
                else:
                    ans = matrix[i][j1] + self.recur(i+1, j1 + new_j1, j2 + new_j2,matrix,r,c,dp)+ matrix[i][j2]
                maxi = max(ans,maxi)
        dp[i][j1][j2] = maxi
        return maxi
    def cherryPickup(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # N*M*M
        dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(m)]
        a = self.recur(0,0,n-1,grid,m,n,dp)
        return a
    