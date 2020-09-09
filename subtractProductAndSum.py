class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        digit = 0
        num = str(n)
        for i in range(len(num)):
            cur = int(num[i])
            product = product * cur
            digit += cur
        result = product - digit
        return result
        