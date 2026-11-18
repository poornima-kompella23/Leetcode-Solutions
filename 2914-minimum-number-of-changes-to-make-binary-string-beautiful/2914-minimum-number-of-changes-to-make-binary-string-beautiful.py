class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        for i in range(0,len(s),2):
            if s[i]!=s[i+1]:
                c+=1
        return c