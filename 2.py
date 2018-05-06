# add two numbers

# 首先是链表数据结构的问题
# 在初始化一个新链表的时候，记得设置两个变量来存储，第一个用于定位头链表，另一个用于next操作
# 单数字相加的时候得注意大于10的情况

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = l3 = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            v1 = v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            carry, val = divmod(v1+v2+carry, 10)

            l3.next = ListNode(val)
            l3 = l3.next
        
        return result.next
