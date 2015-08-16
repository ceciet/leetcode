class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        flag = 0 
        if x < 0:
            flag = 1
            x = (-1) * x
        result = 0
        while x:
            result = result*10 + x % 10
            x = x/10
        if result > 2147483647:
            return 0
        if flag == 1:
            result = (-1) * result
        return result   