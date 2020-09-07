class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ["0"]*len(indices)
        for i in range(len(indices)):
            result[indices[i]] = s[i]
        output = ""
        output = output.join(result)
        return output
            
        