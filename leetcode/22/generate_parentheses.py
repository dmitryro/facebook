class Solution:

        
    def generateParenthesis(self, n: int) -> List[str]:
        C, ans = [], []
        ans = self.generate(C, n, ans, 0, 0)
        return ans

    def generate(self, C, n, ans, op, cl):
        #print(n, op, cl)
        if op < n or cl < n:
            if op < n:
                ans = self.generate(C + ['('], n, ans, op+1, cl)
            if op > cl:
                ans = self.generate(C + [')'], n, ans, op,   cl+1)
        else:
            ans.append(''.join(C))
        return ans        
