# 这个别人的答案，虽然思路和我一样，但是运行速度比我快很多，可以借鉴的操作很多
# * 使用append往list里添加元素.但是如果已知最终大小，先定义一个空list效率会更高
# 但是这么做会产生空格，还得回头删空格
# 可以使用[''] *2 这种形式显示地定义list
# * 使用join

import math

# ! brute force
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1:
            return s
        numLen = math.ceil(len(s)/(2 * numRows - 1))*numRows
        szigzag = [['' for _ in range(numLen)] for _ in range(numRows)]
        irow, icol = 0, 0
        localascend = True
        for si in s:
            szigzag[irow][icol] = si
            if localascend:
                irow += 1
            else:
                irow -= 1
                icol += 1
            if irow == 0:
                localascend =True
            if irow == numRows-1:
                localascend = False
        newS = ''
        for i in range(numRows):
            for j in range(numLen):
                newS = newS if szigzag[i][j] == '' else newS + szigzag[i][j]
        return newS

a = Solution()
print(a.convert('PAYPALISHIRING',3))
print(a.convert('PAYPALISHIRING',4))
print(a.convert('A',1))

# ! 别人的答案
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[] for row in range(numRows)]
        index = 0
        step = -1
        for char in s:
            rows[index].append(char)
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows)

# ! 我改进的答案
# ! str不能s[index] = 'a' 这种方式赋值,要用list，然后join
# 可以跑，但是区别不大
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        numLen = math.ceil(len(s)/numRows) * 2
        rows = [['']* numLen for i in range(numRows)]
        index = 0
        j = 0
        step = 1
        for char in s:
            rows[index][j] = char
            if index == 0 and j > 0:
                step = 1
                j += 1
            elif index == numRows - 1:
                step = -1
                j += 1
            index += step
        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        return ''.join(rows).strip()