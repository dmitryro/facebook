class Solution:

    def __init__(self, w: List[int]):
        self.n = len(w)
        self.lookup = [0] * self.n
        total = 0
        for i in range(self.n):
            total += w[i]
            self.lookup[i] += total

    def pickIndex(self) -> int:
        check = random.randint(1,self.lookup[-1])
        l, r = 0, self.n - 1
        while l < r:
            mid = (l+r)//2
            if check <= self.lookup[mid]:
                r = mid
            else:
                l = mid + 1
        return l



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
