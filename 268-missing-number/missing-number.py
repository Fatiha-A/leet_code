class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set=set(nums)
        for i in range(len(nums)+1):
            if i in num_set:
                continue
            else:
                return i