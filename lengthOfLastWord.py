class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.split(' ')
        for i in range(len(words)-1,-1,-1):
            if words[i]:
                return len(words[i])
        return 0 