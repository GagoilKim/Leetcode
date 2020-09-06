class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            cur = str(nums[i])
            l = len(cur)
            if l % 2 == 0:
                result += 1
        return result
        