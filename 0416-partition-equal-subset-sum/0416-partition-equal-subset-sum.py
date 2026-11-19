
class Solution:
    def recursion(self, index, addi, k, nums, dp):

        if addi == k:
            return True

        if addi > k or index == len(nums):
            return False

        if dp[index][addi] != -1:
            return dp[index][addi]

        # Pick
        pick = self.recursion(
            index + 1, addi + nums[index], k, nums, dp
        )

        # Not Pick
        not_pick = self.recursion(
            index + 1, addi, k, nums, dp
        )

        dp[index][addi] = pick or not_pick

        return dp[index][addi]

    def canPartition(self, nums: list[int]) -> bool:

        target = sum(nums)

        if target % 2 != 0:
            return False

        k = target // 2
        n = len(nums)

        dp = [[-1 for _ in range(k + 1)] for _ in range(n)]

        return self.recursion(0, 0, k, nums, dp)