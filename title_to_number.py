class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        result = 0
        i = 0
        while i < n:
            result += (ord(s[i]) - 64) * pow(26, n-1-i)
            i += 1
        return result
