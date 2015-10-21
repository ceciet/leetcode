class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        else:
            a = 1
            b = 2
            i = 2
            while i < n:
                sum = a + b
                a = b
                b = sum
                i += 1
        return sum

if __name__ == "__main__":
    s = Solution()
    print s.climbStairs(35)