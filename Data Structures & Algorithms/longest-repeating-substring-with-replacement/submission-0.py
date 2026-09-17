class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxFrequency = 0
        result = 0
        count = {}
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1
            maxFrequency = max(maxFrequency,count[s[right]])
            window = right - left + 1
            replacement = window - maxFrequency 
            if replacement > k:
                count[s[left]] = count.get(s[left],0) - 1
                left+=1
            result = max(result, right - left+1)
        return result    
        