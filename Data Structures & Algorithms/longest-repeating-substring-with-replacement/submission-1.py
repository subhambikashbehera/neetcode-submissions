class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        count = {}
        maxFrquency = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right],0)+1   
            maxFrquency = max(maxFrquency,count.get(s[right]))
            widowLength = right - left + 1
            replacement = widowLength - maxFrquency
            if replacement > k:
                count[s[left]] = count.get(s[left],0) - 1
                left += 1
            result = max(result,right-left+1)    
        return result    

