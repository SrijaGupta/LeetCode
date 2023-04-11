#2390 - Removing Stars From a String #https://leetcode.com/problems/removing-stars-from-a-string/description/
class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        si = []

        for i in s:
            if i != "*":
                si.append(i)
            else:
                si.pop()
        return ''.join(si)