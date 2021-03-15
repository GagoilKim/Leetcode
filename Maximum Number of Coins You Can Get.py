class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        count = 0
        piles.sort(reverse=True)
        last = len(piles) - 1
        print(piles)
        pointer = 0
        while pointer < last:
            count += piles[pointer + 1]
            print(pointer)
            pointer += 2
            last -= 1
        return count