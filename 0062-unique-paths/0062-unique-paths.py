class Solution:
    def solve(self,i,j,visited,m,n):
        if i == 0 and j == 0:
            return 1
        if i <0 or i == m or j < 0 or j ==n:
            return 0
        if visited[i][j]!=-1:
            return visited[i][j]
        up = self.solve(i -1, j,visited,m,n)
        left = self.solve(i , j-1,visited,m ,n)

        visited[i][j]= up + left
        return visited[i][j]


    def uniquePaths(self, m: int, n: int) -> int:
        visited = [[-1 for _ in range(n)]for _ in range(m)]
        a = self.solve(m-1,n-1,visited,m ,n)
        return a
        