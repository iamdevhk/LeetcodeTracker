class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newStr=[]
        count=0
        for i in range(0,len(s)):
            if s[i] not in newStr:
                newStr.append(s[i])
                count=max(count,len(newStr))
            else:
                idx=newStr.index(s[i])
                newStr.append(s[i])
                newStr=newStr[idx+1:]
        return count
        