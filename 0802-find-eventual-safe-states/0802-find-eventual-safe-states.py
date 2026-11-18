class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        nodecount = len(graph)
        indegres = [0 for _ in range(nodecount)]
        newgraph = [[] for _ in range(nodecount)]
        for i in range(nodecount):
            for j in graph[i]:
                newgraph[j].append(i)
                indegres[i]+=1
        queue = deque()

        for l in range(nodecount):
            if indegres[l] == 0:
                queue.append(l)
    
        result =[]
        while queue:
            currnode = queue.popleft()
            result.append(currnode)
            for adjnode in newgraph[currnode]:
                indegres[adjnode]-=1
                if indegres[adjnode]==0:
                    queue.append(adjnode)

        result.sort()
        return result