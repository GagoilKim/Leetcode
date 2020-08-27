class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = []
        for i in range(0, len(s) - 11):
            if i == 0:
                if len(s) != 10:
                    if s[9] != s[10]:
                        st = s[0:10]
                        result.append(st)
                else:
                    result.append(s)
            else:
                if s[i-1] != s[i] and s[i+9] != s[i+10]:
                    st = s[i:i+10]
                    result.append(st)
        return result
        