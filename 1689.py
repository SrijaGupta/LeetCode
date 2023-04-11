#1689. Partitioning Into Minimum Number Of Deci-Binary Numbers #https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/

class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        m = 0
        for i in n:
            m = max (m, int(i))
        
        return m
