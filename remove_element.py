class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[start] = nums[i]
                start += 1
        return start

if __name__ == "__main__":
    s = Solution()
    print s.removeElement([1], 1)