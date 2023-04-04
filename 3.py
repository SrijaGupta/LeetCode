#3. Longest Substring Without Repeating Characters #https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = ""
        ml = 0
        for i in range(len(s)):
            if s[i] not in sub:
                sub = sub + s[i]
                ml = max(ml, len(sub))
            elif s[i] in sub:
                ind = sub.index(s[i])
                sub = sub[ind+1:] + s[i]
        return ml