class Solution:
    def hammingWeight(self, n: int) -> int:
        s = str(n)
        s = int(s)
        s = bin(s)
        s = str(s)
        count = 0
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
        return count
        