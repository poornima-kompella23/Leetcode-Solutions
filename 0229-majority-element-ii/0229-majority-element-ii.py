class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=Counter(nums)
        l1=[]
        for p,q in d.items():
            if q>len(nums)/3:
                l1.append(p)
        return l1