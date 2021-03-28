import re

class RomanNumberHelper:
    def __init__(self):
        self.alist = [(1000,'M'), (900,'CM') , (500,'D') , (400 , 'CD'),
                      (100,'C'),(90,'XC'), (50,'L'), (40, 'XL') , 
                      (10,'X'), (9,'IX'), (5,'V'),(4,'IV'),(1,'I')]

    def to_roman(self, num):
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // self.alist[i][0]):
                roman_num += self.alist[i][1]
                num -= self.alist[i][0]
            i += 1
        return roman_num 


if __name__ == "__main__":
    romanNumberals = RomanNumberHelper()
    n = 1234
    b = romanNumberals.to_roman(n)
    print(f"Integer to Roman - {b}")
