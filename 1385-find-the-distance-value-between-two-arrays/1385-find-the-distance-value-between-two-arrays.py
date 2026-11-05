class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        c=0
        arr2=sorted(arr2)
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                c1=abs(arr1[i]-arr2[j])
                if c1<=d:
                    break
            else:
                c+=1
        return c