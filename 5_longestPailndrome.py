"""
LeetCode 5. Longest Palindromic Substring

给定一个字符串 s，找到 s 中最长的回文子串。

Given a string s, return the longest palindromic substring in s.

示例：
    输入：s = "babad"
    输出："bab" 或 "aba"

    输入：s = "cbbd"
    输出："bb"

    输入：s = "a"
    输出："a"
"""

from typing import Tuple


def longest_palindrome(s: str) -> str:
    """
    解法1：中心扩展法（最优解）

    核心思路：
    回文串是对称的，因此可以枚举每一个可能的"中心"，然后从中心向两边扩展。
    中心可以是单个字符（奇数长度回文）或两个字符之间（偶数长度回文）。

    算法步骤：
    1. 遍历字符串中的每个位置 i（0 到 n-1）
    2. 对于每个位置，分别尝试两种中心：
       - 奇数长度：以 i 为中心，向两边扩展
       - 偶数长度：以 i 和 i+1 之间为中心，向两边扩展
    3. 记录扩展过程中最长的回文子串
    4. 返回最长的结果

    代码详解：
    - expand_around_center 函数处理具体的扩展逻辑
    - 当左右字符相等时继续扩展，否则停止
    - 每次扩展后检查是否需要更新最长结果

    复杂度分析：
    - 时间复杂度：O(n²)，n 个中心，每个中心最多扩展 n 次
    - 空间复杂度：O(1)，只使用常数额外空间

    边界情况：
    - 空字符串：返回 ""
    - 单个字符：返回该字符
    - 全部相同字符：返回整个字符串
    - 无回文（长度>1）：返回任意单个字符

    优化点：
    - 相比动态规划 O(n²) 空间，此方法只需 O(1) 空间
    - 不需要预处理，直接扩展即可
    - 实际运行中，大部分中心会很快停止扩展
    """

    if not s:
        return ""

    def expand_around_center(left: int, right: int) -> Tuple[int, int]:
        """
        从中心向两边扩展，寻找最长的回文子串

        参数：
            left: 左边界起始位置
            right: 右边界起始位置

        返回：
            (start, end): 最长回文子串的起止索引（包含）
        """
        # 思考：为什么可以用 while 而不用 if？
        # 因为回文可能有多层，需要一层层向外验证
        while left >= 0 and right < len(s) and s[left] == s[right]:
            # 关键：向两边扩展
            left -= 1
            right += 1

        # 注意：循环结束时，left 和 right 已经超出了回文范围
        # 所以需要回退一步
        return left + 1, right - 1

    start, end = 0, 0  # 记录最长回文子串的起止位置

    for i in range(len(s)):
        # 思考：为什么每次要检查两种情况？
        # 奇数长度回文（如 "aba"）和偶数长度回文（如 "abba"）的中心不同

        # 情况1：奇数长度，以 i 为中心
        left1, right1 = expand_around_center(i, i)
        # 情况2：偶数长度，以 i 和 i+1 之间为中心
        left2, right2 = expand_around_center(i, i + 1)

        # 关键：选择更长的回文子串
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    # 注意：Python 切片是左闭右开，所以是 end + 1
    return s[start:end + 1]


def longest_palindrome_dp(s: str) -> str:
    """
    解法2：动态规划（经典解）

    核心思路：
    使用二维布尔数组 dp[i][j] 表示 s[i:j+1] 是否为回文。
    通过已知的子问题推导更大的问题。

    状态转移：
    - dp[i][j] = (s[i] == s[j]) and (j - i < 2 or dp[i+1][j-1])
    - s[i] == s[j]：首尾字符必须相等
    - j - i < 2：长度为 1 或 2，直接判定
    - dp[i+1][j-1]：去掉首尾后的子串也是回文

    算法步骤：
    1. 初始化 dp 表，所有单个字符都是回文
    2. 按长度递增的顺序遍历所有可能的子串
    3. 对每个子串，根据状态转移方程更新 dp 表
    4. 记录最长的回文子串

    复杂度分析：
    - 时间复杂度：O(n²)，需要填充整个 dp 表
    - 空间复杂度：O(n²)，需要存储 n×n 的 dp 表

    对比说明：
    - 优点：思路清晰，易于理解
    - 缺点：空间复杂度较高，需要 O(n²) 额外空间
    - 适用场景：当需要求解多个子问题时，DP 表可以复用
    """

    if not s:
        return ""

    n = len(s)
    # dp[i][j] 表示 s[i..j] 是否为回文
    dp = [[False] * n for _ in range(n)]

    start, max_len = 0, 1

    # 关键：单个字符都是回文
    for i in range(n):
        dp[i][i] = True

    # 思考：为什么按长度遍历而不是按起点？
    # 因为 dp[i][j] 依赖于 dp[i+1][j-1]，需要先计算短的子串
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # 状态转移方程
            if s[i] == s[j]:
                # 长度为 2 或首尾相等且中间是回文
                if j - i < 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    # 注意：需要在找到更长的回文时更新
                    if length > max_len:
                        start = i
                        max_len = length

    return s[start:start + max_len]


# 测试用例
def run_all_tests() -> None:
    """运行所有测试用例"""
    test_cases = [
        # 题目示例
        ("babad", ["bab", "aba"], "题目示例1"),
        ("cbbd", ["bb"], "题目示例2"),
        ("a", ["a"], "题目示例3"),

        # 边界情况
        ("", [""], "边界: 空字符串"),
        ("aa", ["aa"], "边界: 两相同字符"),
        ("ab", ["a", "b"], "边界: 两不同字符"),

        # 特殊情况
        ("aaaa", ["aaaa"], "特殊: 全相同字符"),
        ("abcde", ["a", "b", "c", "d", "e"], "特殊: 全不同字符"),
        ("abacdfgdcaba", ["aba", "aca"], "特殊: 多个回文"),
        ("abacdedcaba", ["abacdedcaba"], "特殊: 整串是回文"),

        # 复杂情况
        ("cbbd", ["bb"], "复杂: 偶数长度最长"),
        ("bananas", ["anana"], "复杂: 奇数长度最长"),
    ]

    print("=" * 70)
    print("解法1：中心扩展法")
    print("=" * 70)

    passed = 0
    for s, expected_list, desc in test_cases:
        result = longest_palindrome(s)
        # 注意：可能有多个正确答案
        status = "✓" if result in expected_list else "✗"
        if result in expected_list:
            passed += 1

        print(f"{desc}: {status}")
        print(f"  输入: {repr(s)}")
        print(f"  结果: {repr(result)}")
        print(f"  预期: {expected_list}")
        print()

    print(f"通过: {passed}/{len(test_cases)}\n")

    print("=" * 70)
    print("解法2：动态规划")
    print("=" * 70)

    passed = 0
    for s, expected_list, desc in test_cases:
        result = longest_palindrome_dp(s)
        status = "✓" if result in expected_list else "✗"
        if result in expected_list:
            passed += 1

        print(f"{desc}: {status}")
        print(f"  输入: {repr(s)}")
        print(f"  结果: {repr(result)}")
        print(f"  预期: {expected_list}")
        print()

    print(f"通过: {passed}/{len(test_cases)}")


if __name__ == "__main__":
    run_all_tests()
