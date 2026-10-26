class Solution:
    def solve(self,index, total, subset, nums,target, result):
        if total ==0:
            result.append(subset.copy())

        if total<0:
            return

        if index > len(nums):
            return 

        for i in range(index,len(nums)):
            if i > index and nums[i] ==nums[i-1]:
                continue
            subset.append(nums[i])
            remaining = total - nums[i]
            self.solve(i+1,remaining, subset,nums,target, result)
            subset.pop()

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result= []
        self.solve(0,target,[], candidates,target, result)
        return result
        