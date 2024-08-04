class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ptr=0
        for ptr in range(len(nums)):
            for i in range(ptr+1,len(nums)):
                 if nums[ptr]+nums[i]==target:
                    return[ptr,i]
