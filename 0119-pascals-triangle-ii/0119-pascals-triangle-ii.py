class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        l=[]
        for i in range(rowIndex+1):
            l1=[]
            for j in range(i+1):
                l1.append(1)
            l.append(l1)
        for i in range(2,len(l)):
            for j in range(1,len(l[i])-1):
                l[i][j]=l[i-1][j-1]+l[i-1][j]
        return l[rowIndex]