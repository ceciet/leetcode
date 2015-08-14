__author__ = 'baidu'
class Solution:
    def getLetterMaps(self, s):
        d = dict()
        for element in s:
            if d.has_key(element):
                d[element] += 1
            else:
                d[element] = 1
        return d
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        result = cmp(self.getLetterMaps(s), self.getLetterMaps(t))
        if result==0:
            return True;
        else:
            return False;