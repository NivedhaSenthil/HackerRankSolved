# Problem:
#
# Sample Input:
# 5 6 7
# 3 6 10
#
# Sample Output:
# 1 1
#
# Explanation:
#
# In this example:
# A = (a0,a1,a2) = (5,6,7)
# B = (b0,b1,b2) = (3,6,10)
# Now, let's compare each individual score:
#
# a0 > b0, so Alice receives  point.
# a1 = b1 , so nobody receives a point.
# a2 < b2, so Bob receives  point.
# Alice's comparison score is , and Bob's comparison score is . Thus, we print 1 1 (Alice's comparison score followed by Bob's comparison score) on a single line.

# Solution:

a0,a1,a2 = input().strip().split(' ')
a = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b = [int(b0),int(b1),int(b2)]

a_rank = 0
b_rank = 0
count = 0
for i in range(3) :
    if a[i] > b[i]:
        a_rank += 1
    elif b[i] > a[i]:
        b_rank += 1
print (a_rank, b_rank)