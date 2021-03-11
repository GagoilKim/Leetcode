class Solution:
    def interpret(self, command: str) -> str:
        result = command
        result = result.replace("()", "o")
        result = result.replace("(al)", "al")
        print(result)
        return result
        
        