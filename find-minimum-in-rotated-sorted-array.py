class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is []:
            return None

        left = 0
        right = len(nums) - 1

        while left < right - 1:
            mid = (left + right)/2
            if nums[left] < nums[right]:
                return nums[left]
            if nums[left] < nums[mid]:
                left = mid
            else:
                right = mid
        return min(nums[left], nums[right])

    def findMin_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return None

        start = 0
        end = len(nums)-1
        while(start < end-1):
            mid = (start+end)/2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid
        return min(nums[start:end+1])
