class Solution:
    def maximum69Number (self, num: int) -> int:
        n = str(num)
        n = n.replace('6', '9', 1)
        result = int(n)
        return result
        