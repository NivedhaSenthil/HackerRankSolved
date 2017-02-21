# Problem:
#
# Sample Input:
# 2
# 4
# 1 2 3 4
# 6
# 2 -1 2 3 4 -5
#
# Sample Output:
# 10 10
# 10 11
#
# Explanation:
#
# In the first case:
# The max sum for both contiguous and non-contiguous elements is the sum of ALL the elements (as they are all positive).
#
# In the second case:
# [2 -1 2 3 4] --> This forms the contiguous sub-array with the maximum sum.
# For the max sum of a not-necessarily-contiguous group of elements, simply add all the positive elements.

# Solution:

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    curr_max = arr[0]
    sum_arr = arr[0]
    for i in range(1,n):
        sum_arr = max(arr[i], arr[i] + sum_arr)
        curr_max = max(sum_arr,curr_max)
    arr.sort(reverse=True)
    count = 0
    for a in arr:
        if a <= 0:
            break;
        count += 1
    if count is 0: count = 1
    next_curr_max = sum(arr[:count])
    print(curr_max,next_curr_max)