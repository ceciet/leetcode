__author__ = 'baidu'
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True
        # return ((n & (n -1)) == 0);
        while n:
            if n == 2:
                return True

            if n % 2 ==0:
                n = n/2
            else:
                return False
