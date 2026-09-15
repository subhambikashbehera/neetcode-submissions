class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maxS = 0
        
        # for i in range(len(s)):
        #     seen = set()
        #     for j in range(i,len(s)):
        #         if s[j] not in seen:
        #             seen.add(s[j])
        #             maxS = max(maxS,len(seen))
        #         else:
        #             break
        # return maxS          

        # we will be doing with sliding window now
        left = 0
        maxS = 0
        seen = set()
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            maxS = max(maxS,right - left + 1)
        return maxS        






        