from itertools import permutations 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p = permutations(nums)
        
        result = list(p)
        for i in range(len(result)):
            result[i] = list(result[i])
        return result