class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        left = []
        right = [0] * len(nums)
        left_prod = 1
        for i,num in enumerate(nums):
          if(len(left) == 0):
            left_prod = left_prod * 1
          else:
            left_prod = left_prod * nums[i-1]
          left.append(left_prod)
        
        right_prod = 1
        for i in range(len(nums)-1,-1,-1):
          if i == len(nums)-1: 
            right[i] = right_prod
          else:
            right_prod = nums[i+1] * right_prod
            right[i] = right_prod

        for i in range(len(nums)):
          prod = left[i]*right[i]
          result.append(prod)
        
        return result

