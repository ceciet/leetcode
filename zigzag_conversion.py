__author__ = 'baidu'
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s
        s1 = ""
        for i in range(0, numRows):
            s1 += s[i]
            if i==0 or i==numRows-1:
                j = 1
                while 2*j*(numRows-1)+ i < len(s):
                    s1 += s[2*j*(numRows-1)+ i]
                    j += 1
            else:
                j = 1
                while  2*j*(numRows-1) + i < len(s):
                    s1+= s[2*j*(numRows-1) - i]
                    s1+= s[2*j*(numRows-1) + i]
                    j += 1
                if 2*j*(numRows-1) - i <len(s):
                    s1+= s[2*j*(numRows-1) - i]
        return s1