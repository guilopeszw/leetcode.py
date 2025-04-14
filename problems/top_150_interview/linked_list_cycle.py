class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy_node = ListNode()
        dummy_node.next = head
        slow = fast = dummy_node

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False