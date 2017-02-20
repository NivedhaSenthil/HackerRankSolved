# Problem:
#
# Sample Input:
# NULL, data = 3, position = 0
# 3 --> NULL, data = 4, position = 0
#
# Sample Output:
# 3 --> NULL
# 4 --> 3 --> NULL
#
# Explanation:
# 1. we have an empty list and position 0. 3 becomes head.
# 2. 4 is added to position 0, hence 4 becomes head.

#Solution:
"""
 Insert Node at the end of a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
     if position == 0 :
            new_node = Node(data, head)
            return new_node

     previous_node = head
     if head.next is None:
            head.next = Node(data, )
            return head
     current_node = head.next
     for n in range(2, position+1):
            if current_node.next:
                previous_node = current_node
                current_node = current_node.next
     new_node = Node(data,current_node)
     previous_node.next = new_node
     return head