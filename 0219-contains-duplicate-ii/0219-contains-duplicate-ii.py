class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        dict = {}
        for i in range(n):
            a = nums[i]
            if a in dict:
                if abs(dict[a]- i)<=k:
                    return True
            dict[a] = i
        return False


            

        return False


        