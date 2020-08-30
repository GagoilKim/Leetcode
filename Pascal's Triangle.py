class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            cur = [0] * (i + 1)
            cur[0] = 1
            cur[-1] = 1
            print(cur)
            for j in range(1, len(cur) - 1):
                cur[j] = result[i - 1][j - 1] + result[i - 1][j]
            
            result.append(cur)
        return result
            
            
        