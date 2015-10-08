class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        words = s.strip().split()

        for word in words:
            if word not in wordDict:
                return False

        return True
