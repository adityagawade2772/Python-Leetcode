class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left <  right and not s[left].isalnum():# isalnum is bultin method that return true or false like true = A a 5 false = "!"  " " "-"
                left += 1

            while left < right and not s[right].isalnum():
                right -=1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
        