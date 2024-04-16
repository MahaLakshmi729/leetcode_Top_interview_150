from collections import Counter

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        occurrences = Counter(nums)
        for n in nums:
            if occurrences[n] == 1:
                return n