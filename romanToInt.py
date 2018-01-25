class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        romNum = {'M': 1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        result = 0
        
        for j in range(len(s)-1):
            if romNum[s[j]] < romNum[s[j+1]]:
                result -= romNum[s[j]]
            else:
                result += romNum[s[j]]
        
        return result + romNum[s[-1]]
