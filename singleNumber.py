class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            tmp = nums.pop(0)
            if tmp in nums:
                nums.remove(tmp)
            else:
                return tmp
        return nums[0]
            
        