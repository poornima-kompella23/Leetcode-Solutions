class Solution(object):
    def peakValleyDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l1=[]
        l2=[]
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                l1.append(nums[i])
            elif nums[i]<nums[i-1] and nums[i]<nums[i+1]:
                l2.append(nums[i])
        return sum(l1)-sum(l2)