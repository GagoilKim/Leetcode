class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        h = n//2
        for i in range(h):
            for j in range(i, n - i - 1):
                k = n - i - 1
                l = n - j - 1
                matrix[i][j] = matrix[j][k]
                matrix[j][k] = matrix[i][j]
                matrix[l][i] = matrix[i][j]
                matrix[i][j] = matrix[l][i]
                matrix[k][l] = matrix[l][i]
                matrix[l][i] = matrix[k][l]
            
        """
        Do not return anything, modify matrix in-place instead.
        """
        