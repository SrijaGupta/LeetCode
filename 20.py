#20 Valid Parenthesis #https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {"(":")","[":"]","{":"}"}
        arr = []
        s=s.encode("utf-8")
        for i in range(len(s)):
            if s[i] in d:
                arr.append(d[s[i]])
            else:
                if (len(arr)) == 0:
                    return False
                if(arr.pop()) != (s[i]):
                     return False
               
            
        if not arr:
            return True
        else:
            return False