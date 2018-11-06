class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic_func(nums, target)



def baoli_func(nums, target):
    lens = len(nums)
    i = 0
    while i < (lens - 1):
        j = i + 1
        while j <= (lens - 1):
            if (nums[i] + nums[j]) == target:
                return [i, j]
            j = j + 1
        i = i + 1


def dic_func(nums, target):
    zdict = {}  # 利用键值对字典来空间换时间
    index = 0  # 索引从0开始记起
    for i in nums:
        j = target-i
        if j in zdict:
            return[zdict[j], index]
        # 如果没有则把这次寻找匹配的i和i的index存入zdict中
        zdict[i] = index
        index = index+1


if __name__ == '__main__':
    result = dic_func([2,7,11,15], 9)
    print(result)