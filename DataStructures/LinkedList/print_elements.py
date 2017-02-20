# Problem:
#
# Sample Input:
# This example uses the following two linked lists:
# NULL
# 1->2->3->NULL
#  and  are the two head nodes passed as arguments to Print(Node* head).
# Note: In linked list diagrams, -> describes a pointer to the next node in the list.
#
# Sample Output:
# 1
# 2
# 3
#
# Explanation:
# Test Case 0: NULL. An empty list is passed to the method, so nothing is printed.
# Test Case 1: 1->2->3->NULL. This is a non-empty list so we loop through each element, printing each element's data field on its own line.

#Solution

"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""

def print_list(head):
    if not head or head.next: return
    print (head.data)
    print_list(head.next)