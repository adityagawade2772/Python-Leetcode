class Solution:
    def dfs(self, i,j,grid,visited,row,col):
        if i <0 or i==row or j<0 or j==col:
            return
        if grid[i][j]==0:
            return 
        if visited[i][j]==1:
            return
        visited[i][j] = 1
        self.dfs(i-1,j,grid,visited,row,col)
        self.dfs(i,j-1,grid,visited,row,col)
        self.dfs(i+1,j,grid,visited,row,col)
        self.dfs(i,j+1,grid,visited,row,col)
    def numEnclaves(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        visited =[[0 for _ in range(col)]for _ in range(row)]
        r,c = 0, 0
        for c in range(col):
            if grid[r][c]==1 and visited[r][c] != 1:
                self.dfs(r,c,grid,visited,row,col)
        r,c =0,0
        for r in range(row):
            if grid[r][c]==1 and visited[r][c] != 1:
                self.dfs(r,c,grid,visited,row,col)
        r , c =row-1,0
        for c in range(col):
            if grid[r][c]==1 and visited[r][c] != 1:
                self.dfs(r,c,grid,visited,row,col)
        r,c = 0,col-1
        for r in range(row):
            if grid[r][c]==1 and visited[r][c] != 1:
                self.dfs(r,c,grid,visited,row,col)
        count = 0
        for m in range(row):
            for n in range(col):
                if visited[m][n] == 0 and grid[m][n] ==1:
                    count +=1

        return count
            
        