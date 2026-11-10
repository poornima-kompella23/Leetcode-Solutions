class Solution(object):
    def calculateScore(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a1=bin(a)[2:]
        a2=bin(b)[2:]
        s1=a1.count("1")
        s2=a2.count("1")
        if s1>=s2:
            return s1*s2
        return s2/s1