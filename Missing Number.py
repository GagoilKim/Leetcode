class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        array = sorted(nums)
        tmp = 0
        for i in range(length):
            if array[i] == tmp:
                tmp += 1
            else:
                return tmp
        return tmp