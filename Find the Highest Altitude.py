class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        now = 0
        for i in range(len(gain)):
            now += gain[i]
            print(now)
            if highest < now:
                highest = now
        return highest
        
        