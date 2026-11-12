class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        row = len(mat)
        col = len(mat[0])
        visited=[[0 for _ in range(col)]for _ in range(row)]
        distance=[[0 for _ in range(col)]for _ in range(row)]
        queue = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    visited[i][j] = 1
                    queue.append([i,j,0])
        while len(queue) != 0:
            i,j,d = queue.popleft()
            distance[i][j]=d
            for dx, dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                newi= i + dx
                newj = j + dy
                if newi<0 or newi == row or newj<0 or newj==col:
                    continue
                if visited[newi][newj]==1:
                    continue
                visited[newi][newj]=1
                queue.append([newi,newj,d+1])
            
        return distance