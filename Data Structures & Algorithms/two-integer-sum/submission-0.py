class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            complment = target -  num 
            if complment in seen:
                return [seen[complment],i]
            seen[num] = i
        return []