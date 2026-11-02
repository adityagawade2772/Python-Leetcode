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
    def tab(self, nums,c):
        prv = [None for _ in range(c)]
        for i in range(c):
            curr = [None for _ in range(c)]
            for j in range(c):
                if i ==0:
                    curr[j] = nums[i][j]
                else:
                    up = nums[i][j] +prev[j]
                    if j ==0:
                        left = float("inf")
                    else:
                        left = nums[i][j] + prev[j-1]
                    if j >=c-1:
                        right = float("inf")
                    else:
                        right= nums[i][j] + prev[j+1]
                    curr[j] = min(up, left, right)

            prev = curr
        return prev
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        c = len(matrix[0])
        dp = [[200 for _ in range(c)] for _ in range(c)]
        a = self.tab(matrix,c)
        mini = float("inf")
        for i in range(c):
            mini = min(mini, a[i])
        return mini

