from operator import itemgetter

class Solution(object):
    def is_valid_part(self, nums):
        d = dict(zip([str(x) for x in range(1, 10)], [0]*10))
        for n in nums:
            if n != "":
                if n == ".":
                    continue
                if d[n] > 0:
                    return False
                else:
                    d[n] = 1
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for n in board:
            if self.is_valid_part(n) is False:
                return False
        for i in range(9):
            num = [itemgetter(i)(j) for j in board]
            if self.is_valid_part(num) is False:
                return False
        for i in range(3):
            for j in range(3):
                num = []
                for n in [x[0 + 3*i:3 + 3*i] for x in board[3*j:3+3*j]]:
                    num += n
                if self.is_valid_part(num) is False:
                    return False
        return True

if __name__ == "__main__":
    s = Solution()
    a = [[x for x in range(9)] for y in range(9)]
    # for n in a:
    #     print n
    for i in range(3):
        for j in range(3):
            num = []
            for n in [x[0 + 3*i:3 + 3*i] for x in a[3*j:3+3*j]]:
                num += n
            print num
    # # a= ["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"]
    # for i in range(3):
    #     num = []
    #     for n in [x[0 + 3*i:3 + 3*i] for x in a[0 + 3*i:3 + 3*i]]:
    #         num += n
    #     print num
    # print s.isValidSudoku(a)

