class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        m = len(g)
        n = len(s)
        count = 0
        left = 0
        right = 0
        g.sort()
        s.sort()
        while right < n and left<m:
            if g[left]<=s[right]:
                count += 1
                left +=1
                right += 1
            else:
                right +=1
        return count


        