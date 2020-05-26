
# attempt (accepted)
def reverseList(self, head: ListNode) -> ListNode:
	node = head
	nums = []
	
	while node:
		nums.append(node.val)
		node = node.next
	
	dummy = pointer = ListNode(None)

	for _ in range(len(nums)):
		pointer.next = ListNode(nums.pop())
		pointer = pointer.next
	
	return dummy.next

# alt solution (recursive, in place)
def reverseList(self, head, prev=None):
	if not head:
		return prev

	curr, head.next = head.next, prev
	return self.reverseList(curr, head)
