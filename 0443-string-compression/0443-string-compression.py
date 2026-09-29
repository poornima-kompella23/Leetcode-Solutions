class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s=""
        c=1
        for i in range(len(chars)):
            if i<(len(chars)-1) and chars[i]==chars[i+1]:
                c+=1
            else:
                s+=chars[i]
                if c>1:
                    s+=str(c)
                c=1
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)