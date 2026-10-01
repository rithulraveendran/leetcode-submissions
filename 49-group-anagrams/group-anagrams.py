from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams=defaultdict(list)
        res=[]
        for i in strs:
            sorted_i=tuple(sorted(i))
            anagrams[sorted_i].append(i)
        for i in anagrams.values():
            res.append(i)
        return res