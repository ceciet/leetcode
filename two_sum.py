__author__ = 'baidu'
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        d = dict()
        for i, n in enumerate(nums):
            if d.has_key(target - n):
                return [d[target-n]+1, i+1]
            else:
                d[n] = i