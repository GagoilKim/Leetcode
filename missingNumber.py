class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = sorted(nums)
        for i in range(len(l)):
            if i != l[i]:
                return i
            if len(l)-1 == i:
                return i + 1
        