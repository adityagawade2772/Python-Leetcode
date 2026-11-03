class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        n = len(g)
        m = len(s)
        s.sort()
        g.sort()
        left, right, count = 0,0,0
        while left<n and right<m:
            if g[left]<=s[right]:

                left +=1
                right+=1
                count+=1

            else:
                right+=1
        return count