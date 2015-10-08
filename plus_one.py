class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        i = len(digits) - 1
        value = (digits[i] + 1)%10
        flag = (digits[i] + 1)/10
        i -= 1
        result.insert(0, value)
        while i >= 0:
            value = (digits[i] + flag) % 10
            flag= (digits[i] + flag) / 10
            result.insert(0, value)
            i -= 1
        if flag != 0:
            result.insert(0, flag)
        return result

if __name__ == "__main__":
    s = Solution()
    print s.plusOne([1,2,9])