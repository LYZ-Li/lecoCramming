# 两个sorted list， 求混合后的中指
# 这道题对时间复杂度也有要求，0(log(m+n))
# ? 如何计算时间复杂度
# ? 二叉树搜索和改良的二叉树
# * 不考虑时间复杂度的情况下，最简单的做法是使用双指针
# * 二叉树搜索
# * 改良的二叉树搜索

from typing import List
# ! 基于双指针
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        p1, p2 = 0, 0
        
        #使用get_min函数从最小值开始遍历两个list
        # ? 这里的函数为什么不需要传参，直接使用了函数外的变量
        '''这个涉及到的传参问题比较恶心，python也是有空间的说法的，如果在函数
        内部也定义这个变量，那就会优先使用这个内部变量，如果没有定义，那它就会
        自动去函数外找'''
        def get_min():
            nonlocal p1, p2
            # ? 不是说会自动去函数外面找吗，怎么还要用nonlocal拓展
            if p1<m and p2<n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p1 == m:
                ans = nums2[p2]
                p2 += 1
            elif p2 == n:
                ans = nums1[p1]
                p1 += 1
            return ans
        
        #接着从最小的值开始遍历，区分奇数和偶数的情况
        if (m + n) % 2 == 0: #偶数
            for _ in range((m + n)//2 - 1): # ! 这里的结果虽然是个整数，但是除法会强制给你float
                # range的参数只能是int
                _ = get_min() # 这里不需要i也不需要assignment，挪指针就行
            return (get_min() + get_min())/2 
        else:
            for _ in range((m + n)//2 ): #整除,只保留整数部分
                _ = get_min()
            return get_min()
        
a = Solution()
print(a.findMedianSortedArrays([1,3],[2]))
                
print(a.findMedianSortedArrays([1,2],[3,4]))