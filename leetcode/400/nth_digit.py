class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        def totalDigits(i):
            # return the total digits of i-digit number
            start = 10**(i-1)
            end = 10**i-1
            return (end-start+1)*i
        
        i = 1
        total = 0
        prev_total = 0
        # find the level of the digit that n belongs
        while True:
            total += totalDigits(i)
            if n <= total:
                break
            else:
                i += 1
                prev_total = total
        # find the distance from the first number of the level
        distance = n - prev_total-1
        div, mod = divmod(distance, i)
        num = 10**(i-1) + div
        return int(str(num)[mod])
