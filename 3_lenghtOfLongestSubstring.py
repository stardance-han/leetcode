"""
LeetCode 3. Longest Substring Without Repeating Characters

给定一个字符串 s，请你找出其中不含有重复字符的最长子串的长度。

Given a string s, find the length of the longest substring without repeating characters.

示例：
    输入：s = "abcabcbb"
    输出：3
    解释：因为无重复字符的最长子串是 "abc"，所以其长度为 3。

    输入：s = "bbbbb"
    输出：1
    解释：因为无重复字符的最长子串是 "b"，所以其长度为 1。

    输入：s = "pwwkew"
    输出：3
    解释：因为无重复字符的最长子串是 "wke"，所以其长度为 3。
           注意你的答案必须是子串的长度，"pwke" 是一个子序列，不是子串。
"""

import sys
import io
# 设置 stdout 为 UTF-8 编码，支持 emoji 和中文字符
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from typing import Dict


def length_of_longest_substring(s: str) -> int:
    """
    解法1：滑动窗口 + 哈希表（最优解）

    核心思路：
    维护一个滑动窗口 [left, right] 表示当前无重复的子串。
    用哈希表记录每个字符最后出现的位置，当遇到重复字符时，
    可以直接将 left 跳到重复字符之后，而不是逐个移动。

    算法步骤：
    1. 初始化：left = 0, max_len = 0, char_index = {}
    2. 遍历字符串，right 从 0 到 n-1：
       - 如果 s[right] 在 char_index 中且索引 >= left：


        >= left 这个条件是在问：

        ▎ "这个字符上一次出现的位置，是否还在我当前的窗口 [left, right] 范围内？"

        - 是 (>= left)：还在窗口内 → 真正的重复 → 需要处理
        - 否 (< left)：不在窗口内 → 不算重复 → 不用管
        
         说明遇到了重复字符，将 left 更新为 char_index[s[right]] + 1
       - 更新 char_index[s[right]] = right
       - 计算当前窗口长度 right - left + 1
       - 更新 max_len = max(max_len, 当前窗口长度)
    3. 返回 max_len

    代码详解：
    - char_index 存储的是 字符 -> 最后出现位置
    - 条件 "索引 >= left" 很重要，处理重复字符在窗口外的情况
    - 例如 "abba"，right=3 时，s[right]='a'，char_index['a']=0，
      但此时 left=2，0 < 2，说明之前的 'a' 已经不在窗口内了

    复杂度分析：
    - 时间复杂度：O(n)，每个字符最多被访问两次（一次右移，一次作为 left 跳跃）
    - 空间复杂度：O(min(m, n))，其中 m 是字符集大小，n 是字符串长度

    边界情况：
    - 空字符串：直接返回 0
    - 单个字符：返回 1
    - 全部重复：如 "aaaa" 返回 1
    - 全部不重复：如 "abc" 返回 len(s)
    - 重复字符在窗口外：如 "abba"，right=3 时，之前的 'a' 已不在窗口内

    优化点：
    - 相比哈希集合解法，此解法在遇到重复字符时可以"跳跃式"移动 left
    - 不需要逐步缩小窗口（while 循环），减少操作次数
    """
    # 边界情况：空字符串
    if not s:
        return 0

    # char_index 存储 字符 -> 最后出现的索引位置
    char_index: Dict[str, int] = {}
    left = 0          # 滑动窗口左边界
    max_len = 0       # 记录最长无重复子串长度

    for right, char in enumerate(s):
        # 思考：当前字符 char 之前是否出现过？
        # 并且出现的位置要在当前窗口 [left, right) 内
        if char in char_index and char_index[char] >= left:
            # 关键：遇到了重复字符，直接将 left 跳到重复字符之后
            # 这样可以跳过中间所有字符，实现"跳跃式"移动
            left = char_index[char] + 1
            # print(f"遇到重复字符 '{char}'，left 从 {left-1} 跳到 {left}")

        # 更新当前字符的最新位置
        char_index[char] = right

        # 思考：当前窗口 [left, right] 的长度是多少？
        current_len = right - left + 1
        max_len = max(max_len, current_len)
        # print(f"right={right}, char='{char}', window='{s[left:right+1]}', len={current_len}, max_len={max_len}")

    return max_len


def length_of_longest_substring_set(s: str) -> int:
    """
    解法2：滑动窗口 + 哈希集合（经典解法）

    核心思路：
    维护一个滑动窗口 [left, right] 和一个哈希集合。
    集合记录窗口内的所有字符，当遇到重复字符时，
    逐步缩小窗口（不断移动 left）直到窗口内无重复。

    算法步骤：
    1. 初始化：left = 0, max_len = 0, char_set = set()
    2. 遍历字符串，right 从 0 到 n-1：
       - 如果 s[right] 在 char_set 中：
         逐步移除 s[left] 并 left++，直到 s[right] 不在 char_set 中
       - 将 s[right] 加入 char_set
       - 更新 max_len = max(max_len, right - left + 1)
    3. 返回 max_len

    代码详解：
    - char_set 只记录当前窗口内的字符
    - while 循环用于逐步缩小窗口，每次只移除左边一个字符
    - 这个过程保证了窗口始终无重复

    复杂度分析：
    - 时间复杂度：O(2n) = O(n)，最坏情况下每个字符被加入和移除各一次
    - 空间复杂度：O(min(m, n))

    边界情况：
    - 同解法1

    对比说明：
    - 此解法在遇到重复字符时需要逐步缩小窗口（while 循环）
    - 逻辑更直观，适合初学者理解滑动窗口概念
    - 相比解法1，操作次数稍多，但思路更清晰
    """
    # 边界情况：空字符串
    if not s:
        return 0

    char_set = set()  # 记录当前窗口内的字符
    left = 0           # 滑动窗口左边界
    max_len = 0        # 记录最长无重复子串长度

    for right, char in enumerate(s):
        # 思考：当前字符 char 是否已在窗口内？
        while char in char_set:
            # 关键：逐步缩小窗口，移除最左边的字符
            removed_char = s[left]
            char_set.remove(removed_char)
            left += 1
            # print(f"窗口内有重复，移除 '{removed_char}'，left 移到 {left}")

        # 将当前字符加入窗口
        char_set.add(char)

        # 思考：当前窗口 [left, right] 的长度是多少？
        current_len = right - left + 1
        max_len = max(max_len, current_len)
        # print(f"right={right}, char='{char}', window={char_set}, len={current_len}")

    return max_len


def print_test_results(func_name: str, test_cases: list, results: list) -> None:
    """格式化打印测试结果"""
    print(f"\n{'='*60}")
    print(f"测试结果：{func_name}")
    print(f"{'='*60}")

    passed = 0
    for i, (test_case, result) in enumerate(zip(test_cases, results), 1):
        input_str, expected, description = test_case
        status = "[PASS]" if result == expected else "[FAIL]"
        if result == expected:
            passed += 1

        print(f"\n测试 {i}: {description}")
        print(f"  输入: {repr(input_str)}")
        print(f"  预期: {expected}")
        print(f"  实际: {result}")
        print(f"  状态: {status}")

    print(f"\n通过: {passed}/{len(test_cases)}")
    print(f"{'='*60}\n")


def run_all_tests() -> None:
    """运行所有测试用例并对比两种解法"""
    # 定义测试用例：(输入, 预期输出, 说明)
    test_cases = [
        # 题目示例
        ("abcabcbb", 3, "题目示例1: abcabcbb"),
        ("bbbbb", 1, "题目示例2: bbbbb"),
        ("pwwkew", 3, "题目示例3: pwwkew"),

        # 边界情况
        ("", 0, "边界: 空字符串"),
        ("a", 1, "边界: 单个字符"),
        ("aaaa", 1, "边界: 全部重复"),
        ("abcdef", 6, "边界: 全部不重复"),

        # 特殊情况
        ("abba", 2, "特殊: 重复字符在窗口外(abba)"),
        ("a中文b中文", 4, "特殊: 中英文混合"),
        ("😀a😀b", 3, "特殊: 包含emoji"),
    ]

    print("\n" + "="*60)
    print("开始测试两种解法...")
    print("="*60)

    # 测试解法1：哈希表
    results_map = []
    for input_str, expected, _ in test_cases:
        result = length_of_longest_substring(input_str)
        results_map.append(result)

    print_test_results("length_of_longest_substring (哈希表解法)",
                      test_cases, results_map)

    # 测试解法2：哈希集合
    results_set = []
    for input_str, expected, _ in test_cases:
        result = length_of_longest_substring_set(input_str)
        results_set.append(result)

    print_test_results("length_of_longest_substring_set (哈希集合解法)",
                      test_cases, results_set)

    # 对比结果
    print("\n" + "="*60)
    print("解法对比")
    print("="*60)
    print(f"两种解法结果是否一致: {'是 [PASS]' if results_map == results_set else '否 [FAIL]'}")
    print("\n说明：")
    print("- 哈希表解法：遇到重复字符时直接跳跃，更高效")
    print("- 哈希集合解法：逐步缩小窗口，逻辑更直观")
    print("- 两种解法时间复杂度都是 O(n)，但哈希表解法常数更小")
    print("="*60 + "\n")


if __name__ == "__main__":
    run_all_tests()
