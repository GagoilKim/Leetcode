class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    print(words[i])
                    count += 1

                    break
        result = len(words) - count
        return result
        