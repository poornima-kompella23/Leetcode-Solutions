class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        c1=0
        for i in s:
            if i=="(":
                c+=1
            elif i==")":
                if c>0:
                    c-=1
                else:
                    c1+=1
        return c+c1