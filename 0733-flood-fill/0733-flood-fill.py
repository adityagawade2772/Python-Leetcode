class Solution:
    def dfs(self, i,j,visited,initial_color,color,row,col):
        if i<0 or i ==row or j <0 or j == col:
            return
        if visited[i][j] != initial_color:
            return
        visited[i][j] = color
        self.dfs( i-1,j,visited,initial_color,color,row,col)
        self.dfs( i,j-1,visited,initial_color,color,row,col)
        self.dfs( i+1,j,visited,initial_color,color,row,col)
        self.dfs( i,j+1,visited,initial_color,color,row,col)
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        row = len(image)
        col = len(image[0])
        if image[sr][sc]== color:
            return image
        initial_color = image[sr][sc]
        visited = deepcopy(image)
        #self.dfs(sr,sc,visited,initial_color,color,row,col)
        #return visited
        queue = deque()
        visited[sr][sc]= color
        queue.append((sr,sc))
        while len(queue)!= 0:
            i,j = queue.popleft()
            for dx,dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                newi, newj = i + dx, j + dy
                if newi < 0 or newi == row or newj <0 or newj == col:
                    continue
                if visited[newi][newj] != initial_color:
                    continue
                visited[newi][newj] = color
                queue.append((newi,newj))
        return visited
                
        