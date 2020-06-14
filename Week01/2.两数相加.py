#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 1、链表头为低位数，可以开始相加
        # 2、一个tmp保存进位，
        # 3、每次将两个链表元素和tmp求和
        # 4、tmp位为0且链表元素截止时计算完毕
        flag = 0
        resNode = ListNode(0)
        curNode = resNode
        while (flag or l1 or l2):
            flag, cur = divmod(flag + (l1.val if l1 else 0) + (l2.val if l2 else 0), 10)
            curNode.next = ListNode(cur)
            curNode = curNode.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return resNode.next
# @lc code=end

