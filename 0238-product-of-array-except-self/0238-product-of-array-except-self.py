class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        right = 1 
        for i in range(len(nums)):
             result[i]*=right
             right*=nums[i]
        left = 1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=left
            left*=nums[i]
        return result

        