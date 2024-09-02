class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs=dict()
        for str in strs:
            sortedStr=''.join(sorted(str))
            if sortedStr not in sortedStrs:
                sortedStrs[sortedStr]=[]
            sortedStrs[sortedStr].append(str)
        return list(sortedStrs.values())


        
        