class Solution:
    def trimMean(self, arr: List[int]) -> float:
        newarr = sorted(arr)
        five = int(0.05 * len(arr))
#       first 5%
        newarr = newarr[five:]
#       last 5%
        newarr = newarr[:-five]
#       find mean
        total = 0
        for i in range(len(newarr)):
            total += newarr[i]
        return total/(len(newarr))