class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pos= []
        negati= []
        for i in range(0, len(nums)):
            if nums[i] % 2 ==0:
                pos.append(nums[i])
            else:
                negati.append(nums[i])
        result = pos + negati
        return result

        