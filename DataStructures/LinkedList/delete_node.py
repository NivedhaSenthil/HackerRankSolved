# Problem:
#
# Sample Input:
# 1 --> 2 --> 3 --> NULL, position = 0
# 1 --> NULL , position = 0
#
# Sample Output:
# 2 --> 3 --> NULL
# NULL
#
# Explanation:
# 1. 0th position is removed, 1 is deleted from the list.
# 2. Again 0th position is deleted and we are left with empty list.

# Solution:
"""
 Delete Node at a given position in a linked list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Delete(head, position):
    if position == 0:
        return head.next
    curr = head
    for n in range(1, position+1):
        if curr.next:
            prev = curr
            curr = curr.next
    prev.next = curr.next
    return head