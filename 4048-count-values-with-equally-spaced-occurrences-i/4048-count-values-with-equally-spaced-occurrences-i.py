class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in set(nums):
            if nums.count(i)==3:
                l.append(i)
        c=0
        l2=[]
        if l==[]:
            return 0
        for i in l:
            l1=[]
            for j in range(len(nums)):
                if nums[j]==i:
                    l1.append(j)
            l2=[]
            for k in range(len(l1)-1):
                l2.append(abs(l1[k]-l1[k+1]))
            if len(set(l2))==1:
                c+=1
        return c