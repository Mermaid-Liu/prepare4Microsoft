class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    cur,prev=head,None
    while cur:
      cur.next,prev,prev.next=prev,cur,cur.next
    return prev
