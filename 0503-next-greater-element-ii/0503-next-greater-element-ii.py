class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []

        for i in range((n*2 -1),-1,-1):
            while len(stack) != 0 and stack[-1] <= nums[i% n]:
                stack.pop()
            if i<n:
                if stack:
                    ans[i] = stack[-1]
            stack.append(nums[i%n])

        return ans


        