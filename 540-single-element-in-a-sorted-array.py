# Leetcode 540

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        
        while left < right:
            mid = (left + right) // 2
            if mid % 2 != 0:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                left = mid + 2
            else:
                right = mid
                
        return nums[left]

# Time complexity : O(logn)
# Space complexity: O(1)