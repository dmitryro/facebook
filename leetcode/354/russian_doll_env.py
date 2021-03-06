class Solution:    
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) <= 1 or not envelopes:
            return len(envelopes) 
    
        envelopes.sort()
 
        
        dp = [1] *len(envelopes)
        
        for i in range(1, len(envelopes)):
            for j in range(i):
                if (envelopes[i][0] > envelopes[j][0]) and (envelopes[i][1] > envelopes[j][1]):
                        dp[i] = max(dp[i], dp[j] + 1)
        # print(dp)
        return max(dp)
        
