class Solution:
    def dfs(self,i,j,grid,visited,count,m,n):
        if i <0 or i == m or j<0 or j==n:
            return 
        if visited[i][j]==1 or grid[i][j]=="0":
            return
        if visited[i][j] == 0 and grid[i][j]=="1":
            visited[i][j] =1
        self.dfs(i+1,j,grid,visited,count,m,n)
        self.dfs(i,j+1,grid,visited,count,m,n)
        self.dfs(i-1,j,grid,visited,count,m,n)
        self.dfs(i,j-1,grid,visited,count,m,n)
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)]for _ in range(m)]
        queue = deque()
        count = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j]==0 and grid[i][j] =="1":
                    count+=1
                    self.dfs(i,j,grid,visited,count,m,n)

        return count