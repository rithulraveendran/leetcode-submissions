class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0
        if len(s)<3:
            return c
        else:
            l=list(s[:3])
            if (len(l))==len(set(l)):
                c+=1
            for i in range(3,len(s)):
                l.pop(0)
                l.append(s[i])
                if len(l)==len(set(l)):
                    c+=1
        return c
            