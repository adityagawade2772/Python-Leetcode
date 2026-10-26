class Solution:
    def solution(self, index, total, subseq, nums, target, result):
        if total == target:
            result.append(subseq.copy())
            return

        if index >= len(nums):
            return

        if total > target:
            return

        subseq.append(nums[index])
        sum = total + nums[index]
        self.solution(index, sum, subseq,nums, target, result)
        sum = total 
        subseq.pop()
        self.solution(index+1, sum, subseq,  nums,target, result)

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result =[]
        self.solution(0, 0, [], candidates, target,result)
        return result
