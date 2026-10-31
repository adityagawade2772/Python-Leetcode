class Solution:
    def solve(self, index,nums):
        if index<0:
            return 0
        if index == 0:
            return nums[index]
        pick = nums[index] + self.solve(index-2, nums)
        not_pick = 0 + self.solve(index-1, nums)
        return max(pick, not_pick)
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        a = self.solve(n-1, nums)
        return a
        