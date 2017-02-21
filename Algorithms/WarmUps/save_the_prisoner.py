# Problem:
#
# Sample Input:
# 1
# 5 2 1
#
# Sample Output:
# 2
#
# Explanation:
# There are N=5 prisoners and M=2  sweets. Distribution starts at ID number S=1, so prisoner 1 gets the first sweet and prisoner 2 gets the second (last) sweet. Thus, we must warn prisoner 2 about the poison, so we print 2 on a new line.

# Solution:

for _ in range(input()):
    n, m, s = map(int, raw_input().split())
    m %= n
    res = (m + s - 1) % n
    if res == 0:
        res = n
    print res