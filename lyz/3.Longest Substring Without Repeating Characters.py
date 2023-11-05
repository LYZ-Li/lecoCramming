class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}

        left = right = 0
        res = 0 # 记录结果
        while right < len(s):
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            # ? 这里的get方法是这个{}什么类型的变量的
            # solved 05. Nov. 2023
            # 这是一个hashmap 在python里叫dict。 get()方法是取得键值，
            # get(key,default) 是在dict 中没有这个key的时候返回这个默认值，可选参数
            window[c] = window.get(c, 0) + 1
            # 判断左侧窗口是否要收缩
            while window[c] > 1:
                d = s[left]
                left += 1
                # 进行窗口内数据的一系列更新
                window[d] -= 1
            # 在这里更新答案
            res = max(res, right - left)
        return res