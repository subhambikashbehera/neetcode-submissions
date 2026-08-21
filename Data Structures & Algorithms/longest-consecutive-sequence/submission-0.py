class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        for num in numbers:
            if num - 1 not in numbers:
                length = 1
                current = num
                while current + 1 in numbers:
                    length +=1
                    current +=1
                longest = max(longest,length)            
        return longest

        