class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        index = 0
        while index < len(nums):
            if nums[index] != 0:
                nums[start] = nums[index]
                start += 1
            index += 1
        print start
        nums[start: index+1] = [0] * (index-start)

        return nums

if __name__ == "__main__":
    s = Solution()
    print s.moveZeroes([0,1,0,3,12])
