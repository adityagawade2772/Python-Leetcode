class Solution:
    def solverecurssion(self, index, jump, nums):
        id = len(nums)
        if index >= id-1:
            return jump
        min_jump= float("inf")
        for i in range(1, nums[index]+1):
            min_jump= min(min_jump, self.solverecurssion(index+i, jump+1, nums))
        return min_jump
    
    def greedy(self, nums):
        left = 0 
        right = 0
        jump = 0
        while right < len(nums)-1:
            farest =0            
            for i in range(left, right +1):
                farest = max(farest, nums[i]+i)

            left = right+1
            right = farest
            jump +=1
        return jump
        


    def jump(self, nums: list[int]) -> int:
        a = self.greedy(nums)
        return a