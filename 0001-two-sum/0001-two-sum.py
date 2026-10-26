class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        freq= {}
        for i in range(0,n):
            rem = target - nums[i]
            if rem in freq:
                return freq[rem], i
            else:
                freq[nums[i]] = i
        