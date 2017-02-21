# Problem:
#
# Sample Input:
# 6
# 1 2 3 4 10 11
#
# Sample Output:
# 31
#
# Explanation:
# We print the sum of the array's elements, which is:1+2+3+4+10+11=31 .

#Solution:

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print sum(arr)
