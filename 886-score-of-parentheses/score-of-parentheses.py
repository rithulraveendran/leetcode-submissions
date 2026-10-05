class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        l=[0]
        for i in s:
            if i=='(':
                l.append(0)
            else:
                v=l.pop()
                l[-1]+=max(2*v,1)
        return l.pop()