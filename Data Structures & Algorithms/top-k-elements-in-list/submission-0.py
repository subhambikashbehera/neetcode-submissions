class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num,0)+1
        sorted_frequency = sorted(frequency,key = frequency.get,reverse=True)
        return sorted_frequency[:k]

        
