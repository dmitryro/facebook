class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = []
        c = nums.count(0)
        s = 0 if c == len(nums) else 1 # if nums all 0,then s = 0,else s=1 
        for i in nums:
            if i != 0:
                s *= i

        for j in range(len(nums)):
            if nums[j] != 0:  #this number is not 0
                if c == 0:
                    pro.append(s//nums[j]) #0's number is 0，
                else:
                    pro.append(0)  #there has other 0, so the product is 0
            elif nums[j] == 0:  #
                temp = c - 1  #use temp so that 0's number wouldn't change
                if temp == 0:
                    pro.append(s)
                else:
                    pro.append(0)

        return pro  
