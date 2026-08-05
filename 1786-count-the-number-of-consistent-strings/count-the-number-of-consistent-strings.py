class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c=0
        s=set(allowed)
        for i in words:
                flag=True
                for j in i:
                    if j not in s:
                        flag=False
                        break
                if flag:
                    c+=1
        return c