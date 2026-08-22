class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        j = 0
        add = 0
        res = float("-inf")
        for i in range(len(nums)):
            add += nums[i]
            if (i >= k-1):
                avg = add/k
                res = max(avg, res)
                add -= nums[j]
                j += 1
        return res


                