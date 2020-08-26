class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = sorted(nums)
        result = []
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                for k in range(j+1, len(l)):
                    s = l[i] + l[j] + l[k]
                    if s == 0:
                        tmp = [0, 0 , 0]
                        tmp[0] = l[i]
                        tmp[1] = l[j]
                        tmp[2] = l[k]
                        if tmp not in result:
                            result.append(tmp)
        return result