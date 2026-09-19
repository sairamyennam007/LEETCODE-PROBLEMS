class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dic={}
        res=[]
        for st in strs:
            if tuple(sorted(st)) not in dic:
                dic[tuple(sorted(st))]=[st]
            else:
                dic[tuple(sorted(st))].append(st)
        for v in dic:
            res.append(dic[v])
        return res
