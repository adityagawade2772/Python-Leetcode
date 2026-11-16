
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        left = 0
        req = len(need)
        formed = 0

        minlength = float("inf")
        start = 0

        for right in range(len(s)):

            ch = s[right]

            if ch in need:
                window[ch] = window.get(ch, 0) + 1

                if window[ch] == need[ch]:
                    formed += 1

            while formed == req:

                currlen = right - left + 1

                if currlen < minlength:
                    minlength = currlen
                    start = left

                leftchar = s[left]

                if leftchar in need:
                    window[leftchar] -= 1

                    if window[leftchar] < need[leftchar]:
                        formed -= 1

                left += 1

        if minlength == float("inf"):
            return ""

        return s[start:start + minlength]
