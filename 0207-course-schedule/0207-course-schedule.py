from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        n =numCourses
        graph=[[] for _ in range(n)]
        indegres= [0 for _ in range(n)]
        for u,v in prerequisites:
            graph[v].append(u)
            indegres[u]+=1
        queue = deque()
        for i in range(n):
            if indegres[i]==0:
                queue.append(i)
        result= []
        while len(queue)!= 0:
            e =queue.popleft()
            result.append(e)
            for adjnode in graph[e]:
                indegres[adjnode] -=1
                if indegres[adjnode]==0:
                    queue.append(adjnode)       
        
        if numCourses== len(result):
            return True
        else:
            return False
        