class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = {}
        for i in range(len(nums)):
            if nums[i] not in l.keys():
                l[nums[i]] = 1
            else:
                l[nums[i]] += 1
        result = [0] * len(l.keys())
        for i in range(l.keys()):
            if l[i] > :
                
        