# Problem:
#
# Sample Input:
# 1 --> 2 --> NULL
# 2 --> 1 --> 4 --> 5 --> NULL
#
# Sample Output:
# 2
# 1
# 5
# 4
# 1
# 2
#
# Explanation:
# 1. First list is printed from tail to head hence 2,1
# 2. Similarly second list is also printed from tail to head.

#Solution:

"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""

def ReversePrint(head):
    stack = []
    iter = head
    while True:
        if iter:
            stack.append(iter.data)
            iter = iter.next
        else:
            break
    length = len(stack)
    for n in range(0,length):
        print stack.pop()
