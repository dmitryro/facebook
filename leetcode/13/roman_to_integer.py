class Solution:
    def romanToInt(self, s: str) -> int:
        import re
        alist = [(1000,'M'), (900,'CM') , (500,'D') , (400 , 'CD'),
                      (100,'C'),(90,'XC'), (50,'L'), (40, 'XL') , (10,'X'),
                      (9,'IX'), (5,'V'),(4,'IV'),(1,'I')]
        result = 0
        i = 0
        while i < len(alist):
            reg = '^'+alist[i][1]
            if re.search(reg , s) != None:
                result += alist[i][0]
                s = re.sub(reg,'',s)
            else:
                i+=1
        return result
