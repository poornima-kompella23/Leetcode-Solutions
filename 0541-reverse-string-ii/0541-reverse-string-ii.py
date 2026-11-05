class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l=len(s)
        if l<k:
            return s[::-1]
        s1=""
        c=0
        for i in range(0,len(s),k):
            s2=s[i:i+k]
            if c%2==0:
                s1+=s2[::-1]
                c+=1
            else:
                s1+=s2
                c+=1   
        return s1