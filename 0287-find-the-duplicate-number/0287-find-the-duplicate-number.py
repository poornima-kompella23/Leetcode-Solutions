class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=Counter(nums)
        for p,q in nums.items():
            if q>=2:
                return p