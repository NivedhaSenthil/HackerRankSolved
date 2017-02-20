# Problem:
#
# Sample Input:
# NULL , data = 1
# 1 --> NULL , data = 2
#
# Sample Output:
# 1 --> NULL
# 2 --> 1 --> NULL
#
# Explanation:
# 1. We have an empty list, on inserting 1, 1 becomes new head.
# 2. We have a list with 1 as head, on inserting 2, 2 becomes the new head.

"""
 Insert Node at the begining of a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Insert(head, data):
    new_node = Node(data,head)
    return new_node