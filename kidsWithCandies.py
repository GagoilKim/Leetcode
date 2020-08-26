class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = sorted(candies)
        greatest = l[len(l) - 1]
        result = []
        for i in range(len(candies)):
            if candies[i] != greatest:
                after = candies[i] + extraCandies
                if after >= greatest:
                    # result.append("true")
                    result.append(True)

                else:
                    # result.append("false")
                    result.append(False)

            else:
                # result.append("true")
                result.append(True)

        return result
        