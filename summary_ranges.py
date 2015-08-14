__author__ = 'baidu'
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if nums == None or len(nums) == 0:
            return []
        result = []
        begin = 0
        end = 0
        while end < len(nums):
            if end < len(nums) - 1 and nums[end + 1] == nums[end] + 1 :
                end += 1
                continue
            else:
                if begin == end:
                    result.append(str(nums[begin]))
                else:
                    result.append(str(nums[begin]) + "->" + str(nums[end]))
                end += 1
                begin = end
        return result