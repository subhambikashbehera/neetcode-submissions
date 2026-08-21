class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        zeros = nums.count(0)
        if zeros > 1: return [0] * len(nums)
        for num in nums:
            if num != 0:
                product *= num
        result = []

        for num in nums:
            if num == 0:
                result.append(product)
            else:
                result.append(0 if zeros == 1 else int(product / num))

        return result