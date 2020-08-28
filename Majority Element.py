class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if d.get(nums[i]) == None:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        m = 0
        dic = 0
        for i in d.keys():
            if d[i] > m:
                m = d[i]
                dic = i
        return dic
        