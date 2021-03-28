class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        S=sum(nums)-S
        if S%2!=0 or S<0: return 0
        S//=2
        dp=[0]*(S+1)
        dp[0]=1
        for c in nums:
            for j in range(S,c-1,-1):
                dp[j]+=dp[j-c]
        return dp[S]   
