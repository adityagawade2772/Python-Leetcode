class Solution:
    # def set_infi(self, matrix, row, col):
    #     r = len(matrix)
    #     c = len(matrix[0])
        
    #     for i in range(r):
    #         for j in range(c):
    #             if (matrix[i][j]!=0 and(i == row or col ==j)) :
    #                 matrix[i][j]= float("inf")

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        row_0 = [0]*r
        col_0 = [0]*c
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    row_0[i] = -1
                    col_0[j] = -1
        for i in range(r):
            for j in range(c):
                if row_0[i] == -1 or col_0[j] == -1:
                    matrix[i][j]=0
                  

        # for i in range(r):
        #     for j in range(c):
        #         if matrix[i][j]==float("inf"):
        #             matrix[i][j] = 0




       