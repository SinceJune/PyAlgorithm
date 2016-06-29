"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        history = 0
        total = 0
        if s:
            for i in s:
                if i == ' ':
                    if total:
                        history = total
                    total = 0
                else:
                    total = total + 1
            return total if total else history
        else:
            return 0


s = Solution()
print(s.lengthOfLastWord("Hello Wo  "))
