class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
            n1,n2=len(p),len(s)
            if n1>n2:
                return []
            s1c=[0]*26
            s2c=[0]*26
            res=[]
            for i in range(n1):
                s1c[ord(p[i])-ord('a')]+=1
                s2c[ord(s[i])-ord('a')]+=1
            if s1c==s2c:
                res.append(0)
            for i in range(n1,n2):
                s2c[ord(s[i])-ord('a')]+=1
                s2c[ord(s[i-n1])-ord('a')]-=1
                if s1c==s2c:
                    res.append(i-n1+1)
            return res
