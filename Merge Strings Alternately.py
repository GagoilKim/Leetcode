class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count = 0
        result = []
        if len(word1) > len(word2): 
            for i in range(len(word1)):
                result.append(word1[i])
                if i >= len(word2):
                    pass
                else:
                    result.append(word2[i])
        else:
            for i in range(len(word2)):
                if i >= len(word1):
                    pass
                else:
                    result.append(word1[i])
                result.append(word2[i])
                    
                    
                    
        return ''.join(result)
            