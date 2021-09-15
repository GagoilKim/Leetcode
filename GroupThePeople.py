class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        answer = []
        current = groupSizes
        tmp = []
        size = 1
        used = 0
        while len(current) != used:
            for i in range(len(current)):
                if current[i] == size:
                    tmp.append(i)
                    used += 1
                    if len(tmp) == size:
                        answer.append(tmp)
                        tmp = []
            size += 1
        return answer