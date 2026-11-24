class Solution:
    def maxLength(self, nums: List[int]) -> int:
        l1=[]
        for i in range(len(nums)):
            l=[]
            for j in range(i,len(nums)):
                l.append(nums[j])
                l1.append(l.copy())
        l2=[]
        for i in range(len(l1)):
            p=1
            for j in l1[i]:
                p*=j
            c=math.lcm(*l1[i])
            c1=math.gcd(*l1[i])
            if p==c*c1:
                l2.append(len(l1[i]))
        return max(l2)