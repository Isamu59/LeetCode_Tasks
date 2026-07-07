class Solution(object):
    def searchInsert(self, nums, target):
        index = 0;
        end = len(nums) - 1

        while index <= end:
            mid = (index + end) // 2

            if nums[mid] == target:
                return mid;
            elif nums[mid] < target:
                index = mid + 1;
            elif nums[mid] > target:
                end = mid - 1;

        return index;
