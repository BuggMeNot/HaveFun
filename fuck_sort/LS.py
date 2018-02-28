# -*- coding: utf-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 0:
            return s
        bufdict = {}
        
        flag = 1
        i = 0
        temp = s[0]

        while i<len(s)-1:
            
            if s[i+1] == s[i] or temp in bufdict:
                
                temp = s[i+1]
                flag = 1
            else:
                temp = temp + s[i+1]
                
                flag += 1
                bufdict[temp] = flag
            
            i += 1
        #bufdict = sorted(bufdict.items(), key = lambda x:x[1])
        
        result = ''
        
        max_len = 1
        for i,j in bufdict.items():
            if j > max_len:
                max_len = j
                result = i
            
        print bufdict
        return str(result)
    
S = Solution()
s = 'abcdewweeavbcabcd'
S.lengthOfLongestSubstring(s)