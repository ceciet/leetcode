__author__ = 'baidu'
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        d = dict()
        for i, n in enumerate(s):
            if d.has_key(n):
                return i+1
            else:
                d[n] = i