__author__ = 'baidu'
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        d = dict()
        for i, n in enumerate(nums):
            if d.has_key(n):
                return True
            else:
                d[n] = i

        return False