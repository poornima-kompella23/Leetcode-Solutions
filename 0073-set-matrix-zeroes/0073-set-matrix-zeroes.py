class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l=[]
        l1=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    l.append(i)
                    l1.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in l or j in l1:
                    matrix[i][j]=0
