class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        c=0
        res=[]
        sub=list(s[:k])
        v = {'a','e','i','o','u'}
        c = sum(1 for ch in sub if ch in v)
        res.append(c)
        for i in range(k,len(s)):
            o=sub.pop(0)
            sub.append(s[i])
            if o in v:
                c-=1
            if sub[-1] in v:
                c+=1
            res.append(c)
        return max(res)