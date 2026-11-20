class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict = {0:1}
        count = 0 
        prefixsum = 0
        for i in range(len(nums)):
            prefixsum += nums[i]

            curr = prefixsum -k
            if curr in dict:
                count+=dict[curr]
            dict[prefixsum] = dict.get(prefixsum,0)+1

        return count


        