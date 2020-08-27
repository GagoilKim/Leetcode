class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    result += 1
        return result
        