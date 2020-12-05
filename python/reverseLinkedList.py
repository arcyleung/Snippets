# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self)

class Solution:
    stack = []
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return
        self.stack.append(head)
        if head.next == None:
            current = head
            while len(self.stack) > 0:
                current.next = self.stack.pop()
                current = current.next
            current.next = None
            return head
        else:
            return self.reverseList(head.next)

def traverse(n: ListNode):
    # traverse test
    current = n
    while current != None:
        print(current.val)
        current = current.next

nodes = []
for i in range(0, 10):
    n = ListNode(i, None)
    nodes.append(n)

for i in range(0, len(nodes) -1):
    nodes[i].next = nodes[i+1]

# traverse(nodes[0])

sol = Solution()

traverse(sol.reverseList(nodes[0]))
# print(sol.reverseList(nodes[0]))