class Solution:
    def isSafe(self, board,col,row,n):
        durow=row
        ducol=col
        while col >= 0:
            if board[row][col] == "Q":
                return False
            col -=1
        row = durow
        col = ducol
        while col >= 0 and row>=0:
            if board[row][col] =="Q":
                return False
            row -=1
            col-=1
        row = durow
        col = ducol

        while row <n and col >= 0:
            if board[row][col] == "Q":
                return  False
            
            row +=1
            col -=1
        
        return True
            

    def solve(self, col, board, ans, n):
        if col == n :
            ans.append(list(board))
            return

        for row in range(n):
            if self.isSafe(board,col,row,n):
                board[row] = board[row][:col] + "Q"+ board[row][col+1:]
                self.solve(col+1, board,ans,n)
                board[row]= board[row][:col] +"."+ board[row][col+1:]

    def solveNQueens(self, n: int) -> list[list[str]]:
        ans=[]
        board=["."*n for _ in range(n)]

        self.solve(0,board,ans,n)
        return ans