class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]: #if new intervals  end is < originals start, append new interval
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] >intervals[i][1]: #elif new intervals start is ? originals last, append original
                res.append(intervals[i])
            else:
                newInterval=[min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])] #else for start find min of both and for end find max of both 
        res.append(newInterval)
        return res
        