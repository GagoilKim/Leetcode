class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [[1] * m] * n
        for i in range(1, n):
            for j in range(1, m):
                result[i][j] = result[i][j - 1] + result[i - 1][j]
        return result[n - 1][m - 1]