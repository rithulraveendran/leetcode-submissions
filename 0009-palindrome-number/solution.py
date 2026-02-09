class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=0
        rev=0
        y=x
        while y>0:
            num=num*10+y%10
            y//=10
        if num==x:
            return True
        else:
            return False
            
