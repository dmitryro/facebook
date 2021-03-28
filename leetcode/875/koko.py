class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        T: O(n* logk), where k is largest number of bananas in the pile.
        """
        l = 1
        r = max(piles) + 1
        
        def count_hr(k):
            h = 0
            for p in piles:
                h += p // k + 1 if p % k != 0 else p // k
            return h
        
        while l < r:
            m = l + (r-l) // 2
            if count_hr(m) <= h:
                # there might be smaller possible speed k to finish the goal, so we search left side of middle point.
                r = m
            else:
                # there's no solution, we need to increase speed. So, we search our potential solution on right side of middle point.
                l = m + 1
        return l 
