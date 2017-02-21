# Problem:
#
# Sample Input:
# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005
#
# Output:
# 5000000015

# Solution:

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print sum(arr)