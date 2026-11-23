class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(nums)):
            if nums[i]%2==0 and nums[i]%3==0:
                l.append(nums[i])
        if l!=[]:
            return sum(l)/len(l)
        return 0