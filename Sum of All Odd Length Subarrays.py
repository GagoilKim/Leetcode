class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l = len(arr)
        total = 0
        for i in range(1, l + 1):
            if i % 2 == 1:
                start = 0
                end = i
                while end <= l:
                    total += sum(arr[start: end])
                    start += 1
                    end += 1
        return (total)
                