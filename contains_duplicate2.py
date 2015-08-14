__author__ = 'baidu'
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = dict()
        for i, n in enumerate(nums):
            if d.has_key(n) and i - d[n] <= k:
                return True
            else:
                d[n] = i
        return False