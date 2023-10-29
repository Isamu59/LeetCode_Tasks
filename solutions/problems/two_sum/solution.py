class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(0, len(nums)):
            x = target - nums[i] 
            if dict1.get(x) == None:
                dict1[nums[i]] = i
            else:
                return dict1.get(x), i