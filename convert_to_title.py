class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n:
            i = (n-1)%26
            result = chr(65 + i) + result
            n = (n-1)/26
        return result

if __name__ == "__main__":
    s = Solution()
    print s.convertToTitle(26)
