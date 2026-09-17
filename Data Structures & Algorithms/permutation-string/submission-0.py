class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        dict1 = Counter(s1)
        window = {}
        left = 0

        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right],0) + 1
            if right - left + 1 > len(s1):
                window[s2[left]] = window.get(s2[left]) - 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1    
            if dict1 == window:
                return True
        return False                


