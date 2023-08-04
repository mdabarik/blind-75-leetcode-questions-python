class Solution:
    def containsDuplicate(self, nums):
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False

# Time Complexity (TC): O(n) - We iterate through the 'nums' array once.
# Space Complexity (SC): O(n) - In the worst case, we need to store all 'n' elements in the set.
