class Solution(object):
    def get_desc_map(self, l):
        desc = []
        word_set = []
        for i, word in enumerate(l):
            if word in word_set:
                desc[word_set.index(word)].append(i)
            else:
                word_set.append(word)
                desc.append([i])
        return desc

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False
        pattern_desc = self.get_desc_map(pattern)
        str_desc = self.get_desc_map(words)

        return pattern_desc == str_desc


if __name__ == "__main__":
    s = Solution()
    print s.wordPattern("abba","dog cat cat dog")
    print s.wordPattern("abba", "dog cat cat fish")