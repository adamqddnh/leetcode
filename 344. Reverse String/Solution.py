class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(0, length / 2):
            s[i], s[length-i-1] = s[length-i-1], s[i]
