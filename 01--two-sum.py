class Solution:
    def twoSum(self, nums, target):
        ans = [0, 0]
        map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in map:
                map[num] = i
            else:
                ans[0] = i
                ans[1] = map[diff]
        return ans

# TC: O(n), SC: O(n)