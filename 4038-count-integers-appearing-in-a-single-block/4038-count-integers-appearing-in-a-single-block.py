class Solution(object):
    def countSpecialIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=1
        c1=0
        nums.append(0)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                c+=1
            else:
                if nums.count(nums[i])==c or nums.count(nums[i])==1:
                    c1+=1
                    c=1
                c=1
        return c1