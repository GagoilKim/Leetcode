import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num = math.factorial(n)
        if num < 10:
            return 0
        st = str(num)
        count = 0
        for i in reversed(st):
            if i == '0':
                count += 1
            else:
                break
        return count
#         count = 0
        
#         while num % 10 == 0:
#             num = num / 10
#             count += 1
            
#         return count