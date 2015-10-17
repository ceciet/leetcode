class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count +=1
            else:
                if candidate == num:
                    count += 1
                else:
                    count -= 1
        return candidate


if __name__ == "__main__":
    s = Solution()
    print s.majorityElement([3,3,4])