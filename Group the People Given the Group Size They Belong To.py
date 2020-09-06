class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in dic.keys():
                dic[groupSizes[i]].append(i)
            else:
                dic[groupSizes[i]] = [i]
        
        result = []
        for i in dic.keys():
            if len(dic[i]) == dic[i]:
                result.append(dic[i])
            else:
                tmp = dic[i]
                for j in range(len(tmp)):
                    
        