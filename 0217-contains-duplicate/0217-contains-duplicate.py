class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()

        for num in nums :
            if num not in seen:
                seen.add(num)
            elif num in seen:
                return True
        if len(seen) == len(nums):
            return False
        