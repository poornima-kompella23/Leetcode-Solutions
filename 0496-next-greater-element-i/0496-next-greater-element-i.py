class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in range(len(nums1)):
            c=nums2.index(nums1[i])
            l1=nums2[c:]
            if l1!=[]:
                l2=[]
                for j in range(len(l1)):
                    if l1[j]>nums1[i]:
                        l.append(l1[j])
                        l2.append(l1[j])
                        break
                if l2==[]:
                    l.append(-1)
        return l