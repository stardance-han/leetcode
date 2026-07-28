# LeetCode 练习项目指南

## 项目概述

本项目用于系统化练习 LeetCode 题目，培养算法思维和数据结构应用能力。每道题都包含详细的中文注释和思路解析，适合技术面试准备和算法学习。

**项目特色：**
- 详细的教学性注释，适合回顾和讲解
- 多种解法对比，理解算法优化思路
- 全面的测试用例，确保代码正确性
- 统一的代码风格，便于维护和复习

---

## 文件命名规范

### 命名格式

```
{题号}_{英文题目名}.py
```

### 命名示例

- `1_two_sum.py`
- `2_add_two_numbers.py`
- `3_length_of_longest_substring.py`

### 命名规则

- 使用下划线分隔单词
- 题目名使用小写字母
- 题号与题目名之间用下划线分隔
- 避免使用空格和特殊字符

---

## 代码结构规范

### 标准文件模板

```python
"""
LeetCode {题号}. {题目英文名}

{题目中文描述}

{题目英文描述}

示例：
    {示例1}
    {示例2}
"""

from typing import ...  # 必要的类型导入

# 如果需要自定义类
class ClassName:
    def __init__(self, ...):
        ...

# 核心解法1（最优解或推荐解法）
def solution_name(params) -> return_type:
    """
    核心思路：
    [一句话概括算法本质]

    算法步骤：
    1. [第一步]
    2. [第二步]
    ...

    代码详解：
    [关键代码段的具体说明]

    复杂度分析：
    - 时间复杂度：O(...)
    - 空间复杂度：O(...)

    边界情况：
    - [情况1]
    - [情况2]
    ...

    优化点：
    - [为什么这样做更好]
    - [相比其他解法的优势]
    """
    # 实现

# 核心解法2（对比解法，可选）
def solution_name_v2(params) -> return_type:
    """
    对比说明：
    - 此解法与解法1的区别
    - 适用场景
    - 优缺点分析
    """
    # 实现

# 辅助函数（如果需要）
def helper_function(...):
    """[函数用途说明]"""
    ...

# 测试用例
if __name__ == "__main__":
    # 测试代码
```

### 文件结构说明

1. **文件头部文档字符串**（docstring）
   - 题目编号和英文名
   - 题目中英文描述
   - 示例输入输出

2. **导入模块**
   - 优先使用 `from typing import ...` 进行类型注解
   - 只导入必要的模块

3. **自定义类**（如需要）
   - 用于链表、树等数据结构

4. **核心解法函数**
   - 推荐将最优解放在前面
   - 如果有多种解法，按优化程度排序
   - 每个解法都要有详细的 docstring

5. **辅助函数**
   - 用于构建测试数据（如 `build_list()`）
   - 用于验证结果（如 `list_to_nums()`）
   - 用于格式化输出（如 `print_test_results()`）

6. **主程序测试**
   - 包含全面的测试用例
   - 使用 `if __name__ == "__main__":` 保护

---

## 注释写作规范

### 函数级注释（docstring）

每个核心解法函数都应包含完整的 docstring，结构如下：

```python
def solution_name(params) -> return_type:
    """
    解法X：[解法名称]

    核心思路：
    [一句话概括算法本质，回答"为什么这样做"]

    算法步骤：
    1. [第一步的具体操作]
    2. [第二步的具体操作]
    ...

    代码详解：
    - [关键变量或数据结构的用途]
    - [关键代码段的具体说明]
    - [容易出错的地方]

    复杂度分析：
    - 时间复杂度：O(...)，[解释原因]
    - 空间复杂度：O(...)，[解释原因]

    边界情况：
    - [边界情况1及其处理方式]
    - [边界情况2及其处理方式]
    ...

    优化点：
    - [相比其他解法的优势]
    - [为什么这个解法更好]
    """
```

### docstring 各部分说明

#### 1. 核心思路

回答三个问题：
- **为什么**要这样做？
- 解决了什么**核心问题**？
- 用了什么**核心思想**？

示例：
```
核心思路：
使用双指针技巧，一个快指针在前探路，一个慢指针在后构建结果。
快指针跳过重复元素，慢指针只在遇到不重复时才前进。
```

#### 2. 算法步骤

按执行顺序列出具体步骤，每一步都要：
- **具体**：说明做什么
- **清晰**：容易被理解
- **完整**：覆盖整个算法流程

示例：
```
算法步骤：
1. 初始化：left = 0, max_len = 0, char_set = set()
2. 遍历字符串，right 从 0 到 n-1：
   - 如果 s[right] 在 char_set 中：
     逐步移除 s[left] 并 left++
   - 将 s[right] 加入 char_set
   - 更新 max_len = max(max_len, right - left + 1)
3. 返回 max_len
```

#### 3. 代码详解

解释代码中的关键部分：
- **数据结构**：为什么用这个数据结构？
- **关键变量**：存储什么信息？
- **关键逻辑**：为什么要这样写？

示例：
```
代码详解：
- char_set 只记录当前窗口内的字符
- while 循环用于逐步缩小窗口，每次只移除左边一个字符
- 这个过程保证了窗口始终无重复
```

#### 4. 复杂度分析

分别分析时间和空间复杂度：
- **时间复杂度**：说明为什么是 O(n)、O(n²) 等
- **空间复杂度**：说明使用了多少额外空间

示例：
```
复杂度分析：
- 时间复杂度：O(n)，只遍历一次字符串
- 空间复杂度：O(min(m, n))，m 是字符集大小，n 是字符串长度
```

#### 5. 边界情况

列出需要特殊处理的情况：
- **空输入**：空数组、空字符串、空链表
- **单元素**：只有一个元素的输入
- **全相同**：所有元素相同
- **全不同**：所有元素不同

示例：
```
边界情况：
- 空字符串：直接返回 0
- 单个字符：返回 1
- 全部重复：如 "aaaa" 返回 1
- 全部不重复：如 "abc" 返回 len(s)
```

#### 6. 优化点

说明这个解法的优势：
- **相比其他解法**：好在哪里？
- **优化了什么**：时间、空间、代码简洁性？
- **适用场景**：什么时候应该用这个解法？

示例：
```
优化点：
- 相比暴力解法，从 O(n²) 优化到 O(n)
- 使用哈希表记录位置，可以"跳跃式"移动窗口
- 不需要逐步缩小窗口，减少操作次数
```

### 行内注释规范

在代码中使用简短的注释解释关键点：

#### `# 思考：` - 决策点注释

用于解释为什么这样决策：

```python
# 思考：当前字符 char 之前是否出现过？
if char in char_index and char_index[char] >= left:
    # 思考：遇到了重复字符，需要移动 left
    left = char_index[char] + 1
```

#### `# 关键：` - 关键操作注释

用于标记关键的代码段：

```python
# 关键：直接跳跃到重复字符之后，而不是逐步移动
left = char_index[char] + 1
```

#### `# 注意：` - 易错点提醒

用于提醒容易出错的地方：

```python
# 注意：这里要检查索引是否在窗口内，不能只检查是否存在
if char in char_index and char_index[char] >= left:
```

#### 调试注释（开发阶段）

在开发阶段可以使用 `print()` 调试：

```python
# print(f"当前窗口: {s[left:right+1]}, 长度: {current_len}")
```

提交前可以选择注释掉或删除。

---

## 测试用例规范

### 测试用例选择原则

每道题都应该包含全面的测试用例，按以下类别组织：

#### 1. 题目示例（必选）

LeetCode 题目中给出的示例，必须包含。

#### 2. 边界情况（必选）

- **空输入**：空字符串、空数组、None
- **单元素**：只有一个元素
- **全相同**：所有元素相同
- **全不同**：所有元素不同

#### 3. 特殊情况（推荐）

- 算法特定的边界情况
- 需要特殊处理的数据
- 可能触发 bug 的情况

#### 4. 复杂情况（可选）

- 包含特殊字符（Unicode、emoji）
- 大数据量
- 复杂的组合情况

### 测试用例组织方式

#### 方式1：简单测试（适合简单题目）

```python
if __name__ == "__main__":
    # 题目示例
    print(solution([2, 7, 11, 15], 9))  # [0, 1]

    # 边界情况
    print(solution([3, 3], 6))         # [0, 1]

    # 特殊情况
    print(solution([0, 4, 3, 0], 0))   # [0, 3]
```

#### 方式2：结构化测试（推荐）

```python
def run_all_tests() -> None:
    """运行所有测试用例"""
    # 定义测试用例：(输入1, 输入2, 预期输出, 说明)
    test_cases = [
        # 题目示例
        ([2, 7, 11, 15], 9, [0, 1], "题目示例1"),
        ([3, 2, 4], 6, [1, 2], "题目示例2"),

        # 边界情况
        ([], 0, [], "边界: 空数组"),
        ([3, 3], 6, [0, 1], "边界: 两元素相同"),
    ]

    for nums, target, expected, desc in test_cases:
        result = solution(nums, target)
        status = "✓" if result == expected else "✗"
        print(f"{desc}: {status} - 输入:{nums}, 目标:{target}, 结果:{result}")

if __name__ == "__main__":
    run_all_tests()
```

#### 方式3：完整测试框架（适合复杂题目）

```python
def print_test_results(func_name: str, test_cases: list, results: list) -> None:
    """格式化打印测试结果"""
    print(f"\n{'='*60}")
    print(f"测试结果：{func_name}")
    print(f"{'='*60}")

    passed = 0
    for i, (test_case, result) in enumerate(zip(test_cases, results), 1):
        input_data, expected, description = test_case
        status = "✓" if result == expected else "✗"
        if result == expected:
            passed += 1

        print(f"\n测试 {i}: {description}")
        print(f"  输入: {input_data}")
        print(f"  预期: {expected}")
        print(f"  实际: {result}")
        print(f"  状态: {status}")

    print(f"\n通过: {passed}/{len(test_cases)}")
    print(f"{'='*60}\n")

def run_all_tests() -> None:
    """运行所有测试用例"""
    test_cases = [...]  # 定义测试用例

    results = []
    for input_data, expected, _ in test_cases:
        result = solution(input_data)
        results.append(result)

    print_test_results("solution_name", test_cases, results)

if __name__ == "__main__":
    run_all_tests()
```

---

## 按难度分类指南

### 简单题（Easy）

**特点：**
- 思路相对直接
- 通常一种主要解法
- 边界情况较少

**写作要求：**
- **重点**：清晰的问题理解和直观的解法
- **注释**：详细解释思路，适合初学者理解
- **测试**：覆盖题目示例和主要边界情况即可

**示例结构：**
```python
def solution_easy(params):
    """
    核心思路：
    [一句话说明]

    算法步骤：
    1. [...]
    2. [...]

    复杂度分析：
    - 时间复杂度：O(...)
    - 空间复杂度：O(...)

    边界情况：
    - [...]
    """
    # 实现
```

### 中等题（Medium）

**特点：**
- 需要选择合适的算法或数据结构
- 可能有多种解法
- 边界情况和特殊情况较多

**写作要求：**
- **重点**：算法选择、优化思路、多种解法对比
- **注释**：包含复杂度分析和优化点说明
- **测试**：全面的测试用例，包括边界和特殊情况

**示例结构：**
```python
def solution_medium_optimal(params):
    """
    解法1：[最优解] - [算法名]

    核心思路：
    [...]

    算法步骤：
    [...]

    代码详解：
    [...]

    复杂度分析：
    - 时间复杂度：O(...)
    - 空间复杂度：O(...)

    边界情况：
    - [...]

    优化点：
    - 相比暴力解法，优化了 [...]
    """
    # 实现

def solution_medium_classic(params):
    """
    解法2：[经典解] - [算法名]

    对比说明：
    - 此解法与解法1的区别
    - 优缺点分析
    - 适用场景
    """
    # 实现
```

### 困难题（Hard）

**特点：**
- 需要问题分解和高级算法
- 通常需要结合多个算法或数据结构
- 实现细节复杂，容易出错

**写作要求：**
- **重点**：问题分析、算法选择、实现细节
- **注释**：包含问题分析、算法推导、关键代码详解
- **测试**：极端情况和性能测试

**示例结构：**
```python
def solution_hard(params):
    """
    解法：[算法名]

    问题分析：
    - 问题的本质是 [...]
    - 为什么是困难题：[...]
    - 需要解决的关键问题：[...]

    核心思路：
    - 将问题分解为：[...]
    - 使用 [算法/数据结构] 来解决 [...]
    - 关键的优化点：[...]

    算法步骤：
    1. [预处理阶段]
    2. [核心算法阶段]
    3. [结果构造阶段]

    代码详解：
    - [关键数据结构1]：用途和实现
    - [关键数据结构2]：用途和实现
    - [关键逻辑1]：为什么这样处理
    - [关键逻辑2]：边界处理

    复杂度分析：
    - 时间复杂度：O(...)，[详细解释]
    - 空间复杂度：O(...)，[详细解释]

    边界情况：
    - [边界情况1]：处理方式
    - [边界情况2]：处理方式

    优化点：
    - [优化点1]
    - [优化点2]

    注意事项：
    - [容易出错的地方]
    - [性能瓶颈]
    """
    # 实现
```

---

## 按类型分类指南

### 数组/字符串

**常见模式：**
- 双指针
- 滑动窗口
- 哈希表/集合
- 排序 + 双指针

**常用技巧：**
```python
# 双指针 - 一个快一个慢
slow, fast = 0, 0
while fast < len(nums):
    # slow 只在需要时前进
    fast += 1

# 滑动窗口 - 维护一个区间
left, right = 0, 0
while right < len(s):
    # 扩展窗口
    right += 1
    # 缩小窗口
    while condition:
        left += 1
```

**边界情况：**
- 空数组/字符串
- 单元素
- 全相同元素
- 全不同元素

### 链表

**常见模式：**
- 快慢指针
- 哑节点（dummy node）
- 递归
- 迭代

**标准结构：**
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(nums):
    """辅助函数：构建链表"""
    dummy = ListNode()
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next

def list_to_nums(head):
    """辅助函数：链表转列表"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
```

**边界情况：**
- 空链表（head = None）
- 单节点
- 有环链表
- 链表相交

### 二叉树

**常见模式：**
- 递归（DFS）
- 层序遍历（BFS）
- 分治法
- Morris 遍历

**标准结构：**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nums):
    """辅助函数：从列表构建二叉树"""
    if not nums:
        return None
    from collections import deque
    queue = deque()
    root = TreeNode(nums[0])
    queue.append(root)
    i = 1
    while queue and i < len(nums):
        node = queue.popleft()
        if i < len(nums) and nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1
        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1
    return root
```

**边界情况：**
- 空树
- 单节点
- 完全二叉树
- 链状树（所有节点只有左子或右子）

### 动态规划

**常见模式：**
- 一维 DP
- 二维 DP
- 状态压缩
- 记忆化搜索

**解题步骤：**
```python
def solution_dp(params):
    """
    1. 定义状态：dp[i] 表示 [...]
    2. 状态转移：dp[i] = [...]
    3. 初始化：dp[0] = [...]
    4. 遍历顺序：[...]
    5. 返回结果：dp[n]
    """
    n = len(params)
    # 初始化 DP 数组
    dp = [0] * (n + 1)

    # 边界情况
    dp[0] = ...

    # 状态转移
    for i in range(1, n + 1):
        dp[i] = ...

    return dp[n]
```

**边界情况：**
- 最小规模（n=0, n=1）
- 特殊输入（全相同、递增、递减）

### 图

**常见模式：**
- DFS（深度优先搜索）
- BFS（广度优先搜索）
- 并查集
- 最短路径（Dijkstra、Floyd-Warshall）

**标准结构：**
```python
from collections import deque, defaultdict

def build_graph(edges):
    """构建图的邻接表"""
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # 无向图
    return graph

def bfs(graph, start):
    """BFS 模板"""
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**边界情况：**
- 孤立点
- 完全图
- 空图
- 连通分量

---

## 代码风格规范

### 命名规范

- **函数名**：使用小写字母和下划线，如 `two_sum()`、`length_of_longest_substring()`
- **变量名**：使用小写字母和下划线，如 `max_len`、`char_index`
- **常量名**：使用大写字母和下划线，如 `MAX_SIZE`、`DEFAULT_VALUE`
- **类名**：使用驼峰命名，如 `ListNode`、`TreeNode`

### 类型注解

推荐使用类型注解，提高代码可读性：

```python
from typing import List, Optional, Dict, Set

def two_sum(nums: List[int], target: int) -> List[int]:
    ...

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    ...

def length_of_longest_substring(s: str) -> int:
    ...
```

### 代码格式

- 每行不超过 88 字符
- 使用 4 个空格缩进
- 运算符两侧加空格：`max_len = max(max_len, current_len)`
- 逗号后加空格：`def func(a, b, c):`

### import 顺序

```python
# 1. 标准库
from typing import List, Optional

# 2. 第三方库（如果用到）

# 3. 本地模块（如果用到）
```

---

## 项目管理建议

### Git 使用

**Commit 规范：**
```
LeetCode {题号}: {题目名}

示例：
LeetCode 1: Two Sum
LeetCode 3: Longest Substring Without Repeating Characters
```

**分支管理：**
- `master`：主分支，存放完成并测试通过的题目
- 每道题一个 commit，便于追溯

### 文档管理

**建议文件结构：**
```
leetcode/
├── 1_two_sum.py
├── 2_add_two_numbers.py
├── 3_length_of_longest_substring.py
├── CLAUDE.md                          # 本文档
├── README.md                          # 项目介绍（可选）
├── 面试.md                            # 面试记录（已有）
└── docs/                             # 额外文档（可选）
    └── superpowers/
        └── specs/
            └── 2026-07-28-leetcode-3-design.md
```

### 进度跟踪

**建议方式：**
1. 在 GitHub 上创建仓库，使用 Projects 跟踪进度
2. 或在本地维护一个 `PROGRESS.md` 记录已完成题目
3. 按难度分类：简单、中等、困难

**示例进度文件：**
```markdown
# 练习进度

## 数组
- [x] 1. Two Sum
- [x] 3. Longest Substring Without Repeating Characters
- [ ] 11. Container With Most Water
- [ ] 15. 3Sum

## 链表
- [x] 2. Add Two Numbers
- [ ] 19. Remove Nth Node From End of List
- [ ] 21. Merge Two Sorted Lists
```

---

## 附录：常见问题

### Q1: 是否需要包含所有测试用例的运行结果？

A: 不需要。测试用例应该在 `if __name__ == "__main__":` 块中运行，但不需要在代码中保留输出结果。这样可以保持代码简洁，也方便重新测试。

### Q2: 调试用的 print 语句应该保留还是删除？

A: 建议在完成开发和测试后，注释掉调试用的 print 语句，而不是删除。这样在需要调试时可以快速取消注释。例如：

```python
# print(f"当前窗口: {s[left:right+1]}, 长度: {current_len}")
```

### Q3: 多种解法如何排序？

A: 建议按以下优先级排序：
1. **最优解**：时间/空间复杂度最优的
2. **经典解**：思路最直观、最容易理解的
3. **其他解法**：特殊场景适用的解法

### Q4: 何时应该提供多种解法？

A: 以下情况建议提供多种解法：
- 有明显的优化空间（如从 O(n²) 到 O(n)）
- 使用不同的算法思路（如递归 vs 迭代）
- 面试中可能被要求比较不同解法

### Q5: 如何处理 LeetCode 的特定类名（如 Solution）？

A: 本项目不强制使用 LeetCode 的 `Solution` 类，可以直接定义函数。但如果需要提交到 LeetCode，可以在注释中说明如何转换：

```python
def length_of_longest_substring(s: str) -> int:
    """核心解法"""

# 如果需要提交到 LeetCode，使用以下格式：
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         return length_of_longest_substring(s)
```

---

## 总结

本规范的核心目标是：
1. **一致性**：所有题目文件风格统一，便于阅读和维护
2. **教学性**：详细注释帮助理解算法思路和实现细节
3. **完整性**：全面的测试用例确保代码正确性
4. **可读性**：清晰的结构和注释便于回顾和讲解

遵循本规范可以：
- 提高代码质量
- 便于面试准备和算法学习
- 建立系统的知识体系
- 方便与他人分享和讨论

记住：**代码质量比数量更重要，理解思路比死记硬背更有用。**
