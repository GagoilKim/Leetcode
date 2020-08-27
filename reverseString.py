class Solution:
    def reverseString(self, s: List[str]) -> None:
        half = int(len(s)/2)
        for i in range(half):
            l = int(len(s)) - 1
            tmp = s[i]
            s[i] = s[l - i]
            s[l - i] = tmp
            
            
        """
        Do not return anything, modify s in-place instead.
        """
        