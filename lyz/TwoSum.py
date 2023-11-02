# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。
# * 这里给出的是一个哈希映射的解法，但是python本身就有index的操作，不需要这么麻烦
# 想错了， index在找不到对应对象的时候会报错，当然可以使用try： except ValueError
# 但是这么做的效率很低
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 维护 val -> index 的映射
        valToIndex = {}
        for i in range(len(nums)):
            # 查表，看看是否有能和 nums[i] 凑出 target 的元素
            need = target - nums[i]
            if need in valToIndex:
                return [valToIndex[need], i]
            # 存入 val -> index 的映射
            valToIndex[nums[i]] = i
        return []
''' 
# ! chatGPT给出的写法
# 使用了迭代器 enumerate(object, [start]), i 和 num分别是索引和值
# 这种方法是内置的，风格更简单，更pythonic，运算也更快速
# 同时也可以避免range范围计算错误
class Solution:
    def __init__(self, nums):
        self.nums = nums

    def twoSum(self, target):
        num_to_index = {}
        # ? 这里不需要先把这个表建立起来，然后再找吗
        for i, num in enumerate(self.nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

# ! 使用index方法的解法
def twoSum(nums, target):
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums:
            j = nums.index(complement)
            if i != j:
                return [i, j]


# ! 使用双指针的写法
class Solution:
    def twoSum(self, nums, target): # -> List[int]
        '''newnums = nums
        newnums.sort()
        这样不行, 因为newnums并没有创建新的list, 而是指向了旧list的地址
        ''' 
        # ! 这里一定要闲sort，不然这个没法玩
        # ! 因为list也是一种对象，直接给他加.sort()方法就行，不用再赋值nums=nums.sort()
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            left, right = newnums[lo], newnums[hi]
            if left + right < target:
                lo += 1
            elif left + right > target:
                hi -= 1
            else:
                return [nums.index(left), nums.index(right)]
        return []
# 不知道双指针怎么写，因为要的是索引，这种方法只能给出具体值



'''
基于哈希映射的解法的优点：

时间复杂度较低：在平均情况下，基于哈希映射的解法具有较低的时间复杂度 O(n)，其中 n 是输入数组的长度。这是因为哈希表允许快速查找。
更快的解决问题：对于大型输入，基于哈希映射的解法通常比直接使用索引的解法更快。
只需要一次迭代：基于哈希映射的解法只需要一次迭代，而不需要两层嵌套循环。

直接使用索引的解法的优点：

不需要额外的空间：直接使用索引的解法不需要额外的空间来存储哈希表，因此空间复杂度较低。
可能更容易理解：在一些情况下，直接使用索引的解法可能更容易理解，特别是对于初学者来说。\
'''