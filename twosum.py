class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=dict()
        for i in range(0,len(nums)):
            if target-nums[i] in d:
                return (i,d[target-nums[i]])
            else:
                d[nums[i]]=i      