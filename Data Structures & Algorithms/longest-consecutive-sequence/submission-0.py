class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numbers = set(nums)
        for n in numbers:
            if n-1 not in numbers:
                current = n
                length = 1
                while current+1 in numbers:
                    current +=1
                    length +=1
                longest = max(longest,length)     
        return longest 
        