# Problem:
#
# Sample Input:
# 6
#
# Sample Output:
#      #
#     ##
#    ###
#   ####
#  #####
# ######
#
#  Explanation:
#
# The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of n=6.

# Solution:

n = int(raw_input().strip())
for i in range(n):
    spaces = " " * (n-i-1)
    hashes = "#" * (i+1)
    print (spaces + hashes)

