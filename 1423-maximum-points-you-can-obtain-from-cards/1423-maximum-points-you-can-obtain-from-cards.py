class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        nums = cardPoints
        n = len(nums)
        if k ==n:
            return sum(nums)
        left = 0
        right=0
        for i in range(0,k):
            left += nums[i]

        maxi= left
        rightind= n-1

        for i in  range(k-1,-1,-1):
            left -= nums[i]
            right += nums[rightind]
            rightind -=1
            maxi = max(maxi,left+right)
        return maxi
