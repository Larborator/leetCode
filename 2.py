"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0开头。

author: labuladuo
date: 2022/4/13
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def myFunction(l1, l2):
    l3 = ListNode(0)
    p = l1
    q = l2
    now = l3
    carry = 0
    while p or q:
        x = p.val if p else 0
        y = q.val if q else 0
        sum = x + y + carry
        if sum >= 10:
            carry = 1
        else:
            carry = 0
        now.next = ListNode(sum % 10)
        now = now.next
        if p is not None:
            p = p.next
        if q is not None:
            q = q.next
    if carry:
        now.next = ListNode(1)
    return l3.next


if __name__ == '__main__':
    list1 = ListNode(1, ListNode(2, ListNode(3)))
    list2 = ListNode(9, ListNode(9, ListNode(9)))

    resList = myFunction(list1, list2)
    print(resList)
