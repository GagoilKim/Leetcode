class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        result= ""
        for i in range(len(l)):
            cur = []
            for j in reversed(l[i]):
                cur.append(j)
            tmp = ""
            tmp = tmp.join(cur)
            result += tmp + " "
        return result[:-1]
        