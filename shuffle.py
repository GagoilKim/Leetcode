class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        half = int(len(nums)/2)
        result = []
        for i in range(0, half):
            result.append(nums[i])
            result.append(nums[i + half])
        return result