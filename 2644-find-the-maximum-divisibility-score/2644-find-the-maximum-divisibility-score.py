class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(divisors)):
            c=0
            for j in range(len(nums)):
                if nums[j]%divisors[i]==0:
                    c+=1
            l.append(c)
        l1=[]
        for i in range(len(l)):
            if l[i]==max(l):
                l1.append(divisors[i])
        return min(l1)