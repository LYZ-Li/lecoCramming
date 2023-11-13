# 这道题第一眼看上去很简单，就先转成str再reverse然后再转回来
# 实际做起来想要很快且节省空间还是很难的
# ! 尤其最后要判断是不是超过32位，不但要判断原数字，还要判断新数字
class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31 -1 or x < -1 * 2**31 or x == 0:
            return 0

        flag = 1 if x >= 0 else -1
        x = x if x >= 0 else -1 * x
        s = str(x)
        slist=[]
        localflag = 0
        for char in s:
            if char != '0' or localflag ==1 :
                slist.append(char)
                localflag = 1
        slist.reverse()
        newS =''
        for char in slist:
            newS = newS + char
        newX = int(newS) * flag
        if newX > 2**31 -1 or newX < -1 * 2**31:
            return 0
        return newX
    
# !  别人的答案
# python做这道题的人不多
class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 - 1 # 2,147,483,647
        MIN_INT = -2 ** 31    #-2,147,483,648
        reverse = 0

        while x != 0:
            if reverse > MAX_INT / 10 or reverse < MIN_INT / 10:
                return 0
            digit = x % 10 if x > 0 else x % -10
            reverse = reverse * 10 + digit
            x = math.trunc(x / 10) #trunc函数是直接截去小数部分，只保留整数

        return reverse