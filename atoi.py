class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        str = str.lstrip().rstrip()
        flag = 0
        result = 0
        if str.startswith("-"):
            flag = 1
            str = str[1:]
        elif str.startswith("+"):
            flag = 0
            str = str[1:]
        for e in str:
            try:
                n = int(e)
            except e:
                break
            result = result * 10 +n
        if flag == 1:
            result *= (-1)
        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648
        return result