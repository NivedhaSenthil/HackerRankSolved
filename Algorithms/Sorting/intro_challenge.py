# Problem:
#
# Sample Input:
# 4
# 6
# 1 4 5 7 9 12
#
# Sample Output:
# 1
#
# Explanation:
# V=4 . The value 4 is the 2nd element in the array, but its index is 1 since array indices start from 0, so the answer is 1.

# Solution

V = int(input().strip())
N = int(input().strip())
arr = list(map(int,input().strip().split(' ')))

print(arr.index(V))