class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0:
            return False
        right = 0
        left = 0
        n = 0
        x1 = x
        while x1:
            x1 /= 10
            n += 1
        # print n
        while x > 0:
            right = x/pow(10, n-1)
            left = x%10
            # print right, left, n
            if right != left:
                return False
            x = (x - right * pow(10, n-1) - left)/10
            n = n - 2
        return True