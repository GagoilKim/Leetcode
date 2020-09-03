class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic.keys():
                dic[nums[i]] = 1
            else:
                return nums[i]
        