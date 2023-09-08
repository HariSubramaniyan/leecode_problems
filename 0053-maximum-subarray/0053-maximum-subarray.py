class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        current  = 0
        for i in nums:
            if current < 0:
                current = 0
            current = current + i
            maxsum = max(current,maxsum)
        return maxsum
        