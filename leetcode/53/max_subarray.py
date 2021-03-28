class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        t = s = m = nums[0]
        for i in nums:
            if i >= 0:
                s = max(s, 0)
            else:
                m = max(m, s)
            t = max(t, i)
            s += i
        return max(s, m) if t > 0 else t
