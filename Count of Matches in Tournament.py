class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = 0
        while n != 1:
            if n%2 == 0:
                tmp = int(n/2)
                result += tmp
                n = tmp
            else:
                tmp = int((n-1)/2)
                result += tmp
                n = tmp + 1
        return result
                