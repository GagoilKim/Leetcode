class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            cur = s[i]
            t = t.replace(cur, "", 1)
        print(t)
        if len(t) != 0:
            return False
        else:
            return True
        