class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)]for _ in range(m)]
        queue = deque()
        count = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j]==0 and grid[i][j] =="1":
                    count +=1
                    queue.append((i,j))
                    while len(queue)!= 0:
                        dx,dy = queue.popleft()
                        for ni,nj in ((1,0),(0,1),(-1,0),(0,-1)):
                            newi = dx+ni
                            newj= dy+nj
                            if newi<0 or newi== m or newj<0 or newj==n:
                                continue
                            if grid[newi][newj] == "1" and visited[newi][newj]==0:
                                visited[newi][newj]=1
                                queue.append((newi,newj))

        return count