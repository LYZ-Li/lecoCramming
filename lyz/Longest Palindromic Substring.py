# 最大回文子串
# 这道题其实和双指针关系不是很大
# 问题拆分成两个问题
# 1. 判断一个回文string（分奇数和偶数长度的str），应该从中间开始
# 2. 遍历每一个元素为中心的情况，如果找到更长的序列就更新

# 一些细节
# 最后一位不用作为center检查，检查到len(s)-1 位就足够了
# 每一轮都会 l-=1, r+=1, 所以给出substring的时候应该给s[l+1, r],注意这里是r，不用r-1
##   因为r本来就取不到，本来就是取r-1 

#拓展
# 这个问题可以有5种类不同的解法
# 1. 暴力求解 Brute Force
# 2. 中心展开 Expand Around Center （EAC）
# 3. 动态编程 Dynamic Programming （DP）
# 4. Manchester Algorithm （MA）
# 5. Recursive TLE(Time Limit Exceeded)

# ? 什么是动态编程 - 
# ? 什么是Manchester Algorithm
# ? 什么是 recursive
# ? 什么是TLE

#from typing import str # 不知道为什么str不需要额外添加

# ! 双指针的解法 ——labuladong
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i+1)
            res = s1 if len(s1)>len(res) else res
            res = s2 if len(s2)>len(res) else res
        return res



    def palindrome(self, s:str, l:int, r:int) -> str:
        while l>=0 and r<len(s) and s[l]==s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
a = Solution()
print(a.longestPalindrome('babad'))
print(a.longestPalindrome('cbbd'))

# ! brute force
# 就是从第0位开始，看是s[0:n]是不是回文，n-1，n-2...
# 再从第1位开始继续检查，看有没有更长的
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        maxStr = ''
        for i in range(len(s)-1): #最后一位不用检查
            for j in range(i+1, len(s)): # 最后一位在字串里是要检查的
                if j-i+1 > len(maxStr) and s[i:j+1] == s[i:j+1][::-1]:
                    # ! 这里的s[i:j+1] == s[i:j+1][::-1]是highlight，倒序
                    maxStr = s[i:j+1]
        return maxStr
    
# ! dynamic programming

# ? Manchester 没看懂
