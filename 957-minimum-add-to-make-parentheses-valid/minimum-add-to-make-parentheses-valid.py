class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        c=0
        rem=0
        for i in s:
            if i=='(':
                c+=1
            else:
                if c>0:
                    c-=1
                else:
                    rem+=1

        return c+rem