class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mydict= {}
        l,r, maxi=0, 0, 0
        while(r < len(s)):
            if s[r] in mydict:
                l= max(l , mydict[s[r]] + 1)

            maxi = max(maxi, r-l+1)
            mydict[s[r]] = r
            r+=1
        return maxi