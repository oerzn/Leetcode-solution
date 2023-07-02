class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        p = max(candies)
        return [candy + extraCandies >= p for candy in candies]
        
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """