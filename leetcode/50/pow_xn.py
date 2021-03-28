class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: 
            return 1
        if n > 0:
            return self.myPow(x * x, int(n / 2)) * (x if n % 2 else 1)
        else:
            return self.myPow(x * x, int(n / 2)) * (1/x if n % 2 else 1)
