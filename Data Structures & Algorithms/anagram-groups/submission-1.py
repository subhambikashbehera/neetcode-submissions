class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for words in strs:
            key = ''.join(sorted(words))
            groups[key].append(words)
        return list(groups.values())    