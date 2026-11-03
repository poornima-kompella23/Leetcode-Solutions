class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        c=max(nums)
        for i in nums:
            if i==c:
                s+=0
            else:
                s1=c-i
                s+=s1
        return s