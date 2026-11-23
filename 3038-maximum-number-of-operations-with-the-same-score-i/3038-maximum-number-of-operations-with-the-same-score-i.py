class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=2:
            return 1
        c=0
        l=[]
        for i in range(0,len(nums)-1,2):
            s=nums[i]+nums[i+1]
            l.append(s)
        for i in range(len(l)-1):
            if l[i]==l[i+1]:
                c+=1
            else:
                return c+1
        return c+1