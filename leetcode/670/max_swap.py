class Solution:
    def maximumSwap(self, num: int) -> int:
        if not num : return 
        l = list(str(num))
        l = [int(i) for i in l]
        i = 0
        while i < len(l):
            if l[i] != 9:
                temp = l[i+1:]
                if temp :
                    j = self.getLastIndex(temp, max(temp)) + len(l[:i]) + 1
                    if l[i] < l[j]:
                        l[i],l[j] = l[j],l[i]
                        break
            i+=1
        l = [str(i) for i in l]
        return ''.join(l)
    
    def getLastIndex(self,temp,num):
        pos = 0
        for i,n in enumerate(temp):
            if num == n:
                pos = i
        return pos
        
