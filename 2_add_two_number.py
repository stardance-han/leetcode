"""
LeetCode 2. Add Two Numbers

给你两个非空的链表，表示两个非负的整数。
它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式（逆序链表）返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
    输入：l1 = 2 -> 4 -> 3, l2 = 5 -> 6 -> 4
    含义：l1 表示 342，l2 表示 465
    输出：7 -> 0 -> 8   （342 + 465 = 807，逆序输出）
"""

from typing import Optional # Optional 是类型检查工具


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    思路：
    数字是逆序存的，其实正好方便我们模拟“列竖式加法”——
    从最低位（链表头）开始，一位一位往后加，跟小学加法一样，
    区别只是要处理进位（carry）。

    所以：
    1. 同时遍历 l1、l2，每一步把两个节点的值加上上一步的进位 carry。
    2. 这一步的结果里，个位数是新链表这一位的值，十位数（0 或 1）是新的 carry。
    3. 哪个链表短了就当它剩下的位是 0，继续往后走，直到两个链表都走完。
    4. 最后如果还有进位剩余（比如 5+5=10），要多补一位。

    用一个 dummy 头节点简化“新建链表”时对头节点的特殊处理。

    时间复杂度 O(max(m, n))，空间复杂度 O(max(m, n))（新链表长度）。
    """
    dummy = ListNode()  # 占位头节点，方便统一处理，最后返回 dummy.next
    curr = dummy
    carry = 0

    while l1 or l2 or carry:
        # 思考：这一位两个链表分别是多少？没有就当 0
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        # 思考：这一位的和，加上上一位带过来的进位
        total = x + y + carry
        carry = total // 10   # 新的进位
        digit = total % 10    # 这一位留下的数字

        curr.next = ListNode(digit)
        curr = curr.next

        # 思考：两个链表分别往后走一步（如果还有）
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


def build_list(nums: list[int]) -> Optional[ListNode]:
    """辅助函数：把 [2, 4, 3] 这样的列表构造成链表 2->4->3"""
    dummy = ListNode()
    curr = dummy
    for n in nums:
        curr.next = ListNode(n) # 给当前增加一个指向下一个的箭头
        curr = curr.next  # curr 是指针，指向下一个
    return dummy.next # 循环结束后，返回 dummy.next 也就是 整个链表的第一个


def list_to_nums(node: Optional[ListNode]) -> list[int]:
    """辅助函数：把链表转回列表，方便打印验证"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    l1 = build_list([2, 4, 3])   # 342
    l2 = build_list([5, 6, 4])   # 465
    result = add_two_numbers(l1, l2)
    print(list_to_nums(result))  # [7, 0, 8] -> 807

    l1 = build_list([9, 9, 9])   # 999
    l2 = build_list([1])         # 1
    result = add_two_numbers(l1, l2)
    print(list_to_nums(result))  # [0, 0, 0, 1] -> 1000

    l1 = build_list([0])
    l2 = build_list([0])
    result = add_two_numbers(l1, l2)
    print(list_to_nums(result))  # [0]
