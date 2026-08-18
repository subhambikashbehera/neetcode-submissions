class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    #   return len(nums) != len(set(nums))
    #    seen = set()
    #    for num in nums:
    #        if num in seen:
    #          return  True
    #        seen.add(num)
    #    return False    
         nums.sort()
         left = 0
         right = 1
         while right < len(nums):
            if nums[left] == nums[right]:
                return True
            left += 1
            right += 1
         return False        




        