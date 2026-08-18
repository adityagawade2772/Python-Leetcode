class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq= {}
        for i in range(0, len(nums)):
            rem = target - nums[i]
            if rem in freq:
                return freq[rem], i
            else:
                freq[nums[i]]= i
