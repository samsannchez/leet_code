class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            res.append(abs(sum(nums[:i + 1]) - sum(nums[i:])))
        return res