class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in temp:
                return [temp[rem],i]
            temp[num] = i    
        return [0,0]    