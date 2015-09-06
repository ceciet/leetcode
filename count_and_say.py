class Solution(object):
    def generate_str(self, string):
        result = ""
        begin = 0
        end = 0
        while end < len(string):
            if string[end] != string[begin]:
                result = result + str(end - begin) + string[begin]
                begin = end
                end += 1
            else:
                end += 1
        result = result + str(end - begin) + string[begin]
        return result

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        a = list()
        a.append("1")
        for i in range(1, n):
            str = self.generate_str(a[i-1])
            a.append(str)
        return a[n-1]

if __name__ == "__main__":
    s = Solution()
    print s.countAndSay(4)

