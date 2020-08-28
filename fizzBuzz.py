class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for i in range(n):
            cur = i + 1
            if cur % 15 == 0:
                l.append("FizzBuzz")
            elif cur % 3 == 0:
                l.append("Fizz")
            elif cur % 5 == 0:
                l.append("Buzz")
            else:
                l.append(str(cur))
        return l
        