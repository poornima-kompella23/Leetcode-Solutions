class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        l1=[]
        l2=[]
        for i in range(len(grid)):
            l1.append(0)
        for i in range(len(grid[0])):
            l2.append(0)
        for i in range(len(grid)):
            c1=0
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    l2[j]+=1
                    c1+=1
            c=grid[i].count(1)
            l1[i]=c
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    if l1[i]>1 or l2[j]>1:
                        ans+=1
        return ans