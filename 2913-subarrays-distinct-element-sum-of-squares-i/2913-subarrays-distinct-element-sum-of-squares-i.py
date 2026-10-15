class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(nums)):
            l1=[]
            for j in range(i,len(nums)):
                l1.append(nums[j])
                l.append(l1[:])
        l2=[]
        for i in l:
            n=len(set(i))
            l2.append(n*n)
        return sum(l2)