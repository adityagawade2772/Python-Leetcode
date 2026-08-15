class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Handle cases where k is greater than the array length
        k %= n 
        
        # Helper function to reverse elements between two pointers
        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        # Step 1: Reverse the entire array
        reverse(0, n - 1)
                # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the remaining n - k elements
        reverse(k, n - 1)