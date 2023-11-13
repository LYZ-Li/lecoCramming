# 我想到的思路是被labuladong带跑了，直接换成str用双指针
# 双指针在python里不是很好的写法，针对链表的时候更适合一点，list和str不要用双指针
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = x if x >= 0 else x * -1
        s = str(x)
        i,j = 0, len(s)-1
        while i<j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
# ! 网上的神级代码，一模一样的思路，但是更少的代码
def isPalindrome(self, x: int) -> bool:
	if x < 0:
		return False
	
	return str(x) == str(x)[::-1]

# ! 这个代码没有特别惊艳了，但是思路非常好
# * Rabin Karp 算法详解————看labuladong
# # 从第7题衍生来的
# 让原数整除10，每次少一位
# 新数乘10 加 余数
# 新数比余数大之后，比较两个数是不是一样（偶数位数），或者给新数整除10（奇数位数）
def isPalindrome(self, x: int) -> bool:
	if x < 0 or (x > 0 and x%10 == 0):   
		# if x is negative, return False. if x is positive and last digit is 0, 
        # that also cannot form a palindrome, return False.
		return False
	
	result = 0
	while x > result:
		result = result * 10 + x % 10
		x = x // 10
		
	return True if (x == result or x == result // 10) else False