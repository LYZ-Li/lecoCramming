class Solution:
    def myAtoi(self, s: str) -> int:
        maxN = 2**31 -1
        minN = -1 * (maxN + 1)
        myNum = 0
        flag = 0
        for char in s:
            if char == ' ':
                continue
            elif char == '-':
                flag = -1
            elif char >= '0' and char <= '9':
                myNum = myNum * 10 + int(char)
                if myNum > maxN - flag:
                    return maxN if flag==0 else minN
        return myNum if flag==0 else myNum * -1
    
# 评测说这个不行，因为 “words and 987” 应该输出0，而不是987，我有点搞不懂了

# ! 网上的答案，
# 看不懂，用了很多python函数
# ? 正则表达式？

import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s):
            if not s[0].isalpha():
                i = re.search(r"^(-\d+)|^(\+\d+)|^(\d+)",s)
                if i is not None:
                    i = int(i.group())
                    if i < 0:
                        return max(-2**31, i)
                    return min(2**31 - 1, i)
        return 0

# ! 用DFA算法
# ? 什么是DFA
class Solution:
    def myAtoi(self, str: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        if len(str) == 0:
            return 0

        while pos < len(str):
            current_char = str[pos]
            if state == 0:
                if current_char == " ":
                    state = 0
                elif current_char == "+" or current_char == "-":
                    state = 1
                    sign = 1 if current_char == "+" else -1
                elif current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 2:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    break
            else:
                return 0
            pos += 1

        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value
    

# ! 这个方法又快又小，仔细看看
# ? 
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0:
            return 0
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        else:
            sign = 1
        digits = []
        for c in s:
            if c.isdigit():
                digits.append(c)
            else:
                break
        if len(digits) == 0:
            return 0
        else:
            num = int(''.join(digits))
            num *= sign
        num = max(num, -2**31)
        num = min(num, 2**31 - 1)
        return num
    
    # 看完这个我又想到一个前后双指针的思路，前指针负责找符号和数字，后指针把数字复制过来! 不行，str不能这么改，需要额外的list或者str
    # 最后输出一个空 ''.join