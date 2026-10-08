class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        ans = ""
        for i in s:
            if i == "(":
                if count > 0:
                    ans += i
                count += 1
            elif i == ")":
                count -= 1
                if count > 0:
                    ans += i
        return ans