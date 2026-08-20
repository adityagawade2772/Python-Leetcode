class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        positive, negative = 0, 1
        for i in range(0, len(nums)):
            if nums[i]>0:
                ans[positive] = nums[i]
                positive+=2

            else:
                ans[negative] =  nums[i]
                negative += 2
        return ans
            