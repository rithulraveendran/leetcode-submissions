class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pasc=[]
        for i in range(numRows):
            r=[1]*(i+1)
            for j  in range (1,i):
                r[j]=pasc[i-1][j-1]+pasc[i-1][j]
            pasc.append(r)
        return pasc

