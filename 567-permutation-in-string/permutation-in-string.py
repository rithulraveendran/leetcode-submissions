class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        a = [0] * 26
        b = [0] * 26
        
        for i in range(len(s1)):
            a[ord(s1[i]) - 97] += 1
            b[ord(s2[i]) - 97] += 1
            
        if a == b:
            return True
            
        for i in range(len(s1), len(s2)):
            b[ord(s2[i]) - 97] += 1
            b[ord(s2[i - len(s1)]) - 97] -= 1
            if a == b:
                return True
                
        return False