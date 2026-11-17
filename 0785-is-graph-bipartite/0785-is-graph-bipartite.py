class Solution:
    def dfs(self, node, color, visited, graph):

        visited[node] = color

        for adj in graph[node]:

            if visited[adj] == -1:

                ans = self.dfs(adj, 1 - color, visited, graph)

                if ans == False:
                    return False

            elif visited[adj] == color:
                return False

        return True

    def isBipartite(self, graph: list[list[int]]) -> bool:

        n = len(graph)
        visited = [-1] * n

        for i in range(n):

            if visited[i] == -1:

                ans = self.dfs(i, 0, visited, graph)

                if ans == False:
                    return False

        return True