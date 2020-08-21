# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        prev = None
        temp = None

        while (l1 is not None or l2 is not None):
            sum = l1.val + l2.val
            if sum < 10:
                result = ListNode(sum)
                result.next = self.addTwoNumbers(l1.next, l2.next)
                return result
            else:
                sum = l1.val + l2.val-10
                result = ListNode(sum)
                result.next = self.addTwoNumbers(
                    ListNode(1), self.addTwoNumbers(l1.next, l2.next))
                return result


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(0)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    result = Solution().addTwoNumbers(l1, l2)
    while result:
        print(result.val),
        result = result.next
