class Solution:
  #97.54%
  def reverseList(self, head: ListNode) -> ListNode:
    cur,prev=head,None
    while cur:
      cur.next,prev,prev.next=prev,cur,cur.next
    return prev
