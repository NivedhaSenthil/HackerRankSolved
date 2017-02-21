# Sample Input
#
# 6
# -4 3 -9 0 4 1
# Sample Output
#
# 0.500000
# 0.333333
# 0.166667
# Explanation
#
# There are 3 positive numbers, 2 negative numbers, and  1 zero in the array.
# The respective fractions of positive numbers, negative numbers and zeroes are 3/6 = 0.500000 , 2/6 = 0.333333 and 1/6 = 0.166667, respectively.

# Solution:

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

print (len(list(filter(lambda x: x > 0, arr)))/n)
print (len(list(filter(lambda x: x < 0, arr)))/n)
print (len(list(filter(lambda x: x == 0, arr)))/n)