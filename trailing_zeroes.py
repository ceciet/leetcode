class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n:
            ret += n/5
            n /= 5
        return ret

if __name__ == "__main__":
    s = Solution()
    print s.trailingZeroes(25)