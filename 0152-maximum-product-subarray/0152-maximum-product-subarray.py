class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        maxproduct = nums[0]
        minproduct = nums[0]
        pro = nums[0]
        for j in range(1,n):
            if nums[j]<0:
                maxproduct,minproduct = minproduct,maxproduct
            maxproduct = max(nums[j], maxproduct * nums[j])
            minproduct = min(nums[j], minproduct * nums[j])
            pro = max(maxproduct, pro)
        return pro
            
        return maxproduct
        