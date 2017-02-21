# Problem:
#
# Sample Input:
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
#
# Sample Output:
# 15
#
# Explanation:
#
# The primary diagonal is:
# 11
#       5
#             -12
#
# Sum across the primary diagonal: 11 + 5 - 12 = 4
#
# The secondary diagonal is:
#             4
#       5
# 10
# Sum across the secondary diagonal: 4 + 5 + 10 = 19
# Difference: |4 - 19| = 15

# Solution:


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

def first_diagonal_sum(a,n):
    count = n-1
    diagonal_values = []
    for row in a:
        diagonal_values.append(row[count])
        count = count - 1
    return sum(diagonal_values)

def second_diagonal_sum(a):
    count = 0
    diagonal_values = []
    for row in a:
        diagonal_values.append(row[count])
        count = count + 1
    return sum(diagonal_values)

print (abs(first_diagonal_sum(a,n) - second_diagonal_sum(a)))