class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        l=[]
        s1=""
        l1=[]
        nums1=[]
        for i in nums:
            nums1.append(str(i))
        for i in range(len(nums1)):
            n1=nums1[:i+1]
            n1="".join(n1)
            l.append(int(n1,2))
            s1=""
            if l[i]%5==0:
                l1.append(True)
            else:
                l1.append(False)
        return l1