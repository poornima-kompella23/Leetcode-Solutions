class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        c1=0
        c2=0
        for i in range(len(s)):
            if s[i]=="*":
                if c1==0:
                    c2+=1
            elif s[i]=="|":
                if c1%2==0:
                    c1+=1
                else:
                    c1=0
        return c2