class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        j = 0
        while j < len(nums) - 1:
            j += 1
            if nums[j] == nums[j - 1]:
                continue
            else:
                i += 1
                nums[i] = nums[j]

        return i+1

if __name__ == "__main__":
    s = Solution()
    print s.removeDuplicates([])