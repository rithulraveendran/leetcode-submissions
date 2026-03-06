class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        valid={")":"(",'}':'{',']':'['}
        for i in s:
            if i in '({[':
                arr.append(i)
            else:
                if arr:
                    top=arr.pop()
                    if top!=valid[i]:
                        return False
                else:
                    return False
        return len(arr)==0
