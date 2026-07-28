"""
LeetCode 1. Two Sum

给定一个整数数组 nums 和一个整数目标值 target，
请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。

假设每种输入只会对应一个答案，且同一个元素在答案里不能重复出现。
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    思路：
    暴力解法是两层循环枚举所有组合，时间复杂度 O(n^2)。
    但其实我们只需要知道“之前是否出现过某个数”，
    这正好是哈希表(dict)的强项 —— 查找是 O(1)。
    所以换个角度想：遍历到 num 时，我们要找的另一半是 complement = target - num。
    只要提前把“遍历过的数字 -> 下标”记下来，
    每走一步就查一下 complement 是否已经出现过，
    如果出现过，说明之前那个数 + 当前这个数 正好等于 target，直接返回。
    如果没出现过，就把当前的 num 记下来，留给后面的数字去匹配。
    这样只需要一次遍历，时间复杂度降到 O(n)，空间复杂度 O(n)。
    :param nums: 整数数组
    :param target: 目标和
    :return: 两个数的下标组成的列表
    """
    seen = {}  # 记录 值 -> 下标，相当于“记忆”走过的数字
    for i, num in enumerate(nums):
        # 思考：我现在拿到的数是 num，凑成 target 还差多少？
        complement = target - num
        print(f"当前 num={num}, 需要的另一半 complement={complement}, 已记录的 seen={seen}")

        # 思考：这个“另一半”之前是不是已经出现过了？
        if complement in seen:
            # 出现过！说明找到答案了，不用再往后找了
            return [seen[complement], i]

        # 没找到匹配，把当前数字记下来，说不定后面的数字会需要它
        seen[num] = i

    # 思考：遍历完了还没找到，说明题目假设的“必有解”没有满足
    raise ValueError("没有找到符合条件的两个数")


if __name__ == "__main__":
    print(two_sum([2, 6, 11, 15,7], 9))   # [0, 1]
    # print(two_sum([3, 2, 4], 6))        # [1, 2]
    # print(two_sum([3, 3], 6))           # [0, 1]
