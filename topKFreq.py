class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=dict()
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d=sorted(d.items(),key = lambda x :x[1],reverse=True)
        arr=[]
        for i in range(k):
            arr.append(d[i][0])
        return arr