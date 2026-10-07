class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        k=k%len(s)
        for i in range(len(s)):
            s1=s[i:i+k]
            s2=s[i+k:]
            return s2+s1