class Solution(object):
    def get_common_prefix(self, str1, str2):
        prefix = ""
        i = 0
        j = 0
        if len(str1) == 0 or len(str2) == 0:
            return ""
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                prefix = prefix + str1[i]
            else:
                break
            i += 1
            j += 1
        return prefix

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        common = strs[0]
        for i in range(1, len(strs)):
            common = self.get_common_prefix(common, strs[i])
        return common
        