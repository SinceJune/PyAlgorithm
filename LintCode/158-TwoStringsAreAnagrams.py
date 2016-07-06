"""
Write a method anagram(s,t) to decide if two strings are anagrams or not.

Have you met this question in a real interview? Yes
Clarification
What is Anagram?
- Two strings are anagram if they can be the same after change the order of characters.

Example
Given s = "abcd", t = "dcab", return true.
Given s = "ab", t = "ab", return true.
Given s = "ab", t = "ac", return false.
"""


class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """

    def anagram(self, s, t):
        return sorted(s) == sorted(t)
