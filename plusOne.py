class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] != 10:
                return digits
            else:
                digits[i] = 0
        digits = [1] + digits   
                    
            
        return digits
        