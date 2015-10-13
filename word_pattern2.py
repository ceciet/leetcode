__author__ = 'baidu'
import unittest


class Solution(object):

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")

        if len(pattern) != len(words):
            return False

        dictionary = {}

        for i, letter in enumerate(pattern):
            if letter not in dictionary.keys():
                if words[i] in dictionary.values():
                    return False
                else:
                    dictionary[letter] = words[i]
            else:
                if words[i] != dictionary[letter]:
                    return False
        return True




class TestSolution(unittest.TestCase):

    def test_wordPattern(self):
        s = Solution()
        pattern = "abba"
        str = "dog cat cat dog"
        self.assertTrue(s.wordPattern(pattern, str))

        pattern = "abba"
        str = "dog cat cat fish"
        self.assertFalse(s.wordPattern(pattern, str))

        pattern = "aaaa"
        str = "dog cat cat dog"
        self.assertFalse(s.wordPattern(pattern, str))

        pattern = "abba"
        str = "dog dog dog dog"
        self.assertFalse(s.wordPattern(pattern, str))

        pattern = "abb"
        str = "dog dog dog dog"
        self.assertFalse(s.wordPattern(pattern, str))

if __name__ == '__main__':
    unittest.main()