class Solution(object):
    def get_sqrt_sum(self, n):
        numbers = []
        while n:
            numbers.append(n%10)
            n /= 10
        result = sum([i*i for i in numbers])
        return result

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        showed_number = set()
        while True:
            n = self.get_sqrt_sum(n)
            if n == 1:
                return True
            else:
                if n in showed_number:
                    return False
                else:
                    showed_number.add(n)


if __name__ == "__main__":
    s = Solution()
    print s.isHappy(37)