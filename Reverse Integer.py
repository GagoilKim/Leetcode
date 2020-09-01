class Solution:
    def reverse(self, x: int) -> int:
        
        if len(str(x)) == 1:
            return x
        x = str(x)
        result = ''
        for i in reversed(x):
            result += i
        cur = int(result)
        if cur >= 2**31-1 or cur <= -2**31:
            return 0
        
        
        for i in range(len(result)):
            if result[0] == '0':
                result = result[1:]
        if result[-1] == '-':
            result =  result[:-1]
            result = '-' + result
        return result
#             if i == '-':
                
#                 result = '-'  + result
                
#             else:
#                 result += i
#                 if result[0] == '0':
#                     result = result[1:]
        
        return result