class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        l=[]
        l1=[]
        for i in words:
            s=i[::-1]
            l.append(s)
            if i==s:
                l1.append(i)
        if len(l1)!=0:
            return l1[0]
        else:
            return ""