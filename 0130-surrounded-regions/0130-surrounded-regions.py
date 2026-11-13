class Solution:
    def dfs(self,i,j,board,visited,row,col):
        if i <0 or i==row or j<0 or j==col:
            return
        if board[i][j]=="X":
            return 
        if visited[i][j]==1:
            return
        visited[i][j] = 1
        self.dfs(i-1,j,board,visited,row,col)
        self.dfs(i,j-1,board,visited,row,col)
        self.dfs(i+1,j,board,visited,row,col)
        self.dfs(i,j+1,board,visited,row,col)
        


    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        visited =[[0 for _ in range(col)]for _ in range(row)]
        r,c = 0, 0
        for c in range(col):
            if board[r][c]=="O" and visited[r][c] != 1:
                self.dfs(r,c,board,visited,row,col)
        r,c =0,0
        for r in range(row):
            if board[r][c]=="O" and visited[r][c] != 1:
                self.dfs(r,c,board,visited,row,col)
        r , c =row-1,0
        for c in range(col):
            if board[r][c]=="O" and visited[r][c] != 1:
                self.dfs(r,c,board,visited,row,col)
        r,c = 0,col-1
        for r in range(row):
            if board[r][c]=="O" and visited[r][c] != 1:
                self.dfs(r,c,board,visited,row,col)
        for m in range(row):
            for n in range(col):
                if visited[m][n] == 0 and board[m][n] =="O":
                    board[m][n] = "X"
            

