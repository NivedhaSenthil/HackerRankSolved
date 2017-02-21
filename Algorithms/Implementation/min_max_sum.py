# Problem:
#
# Sample Input:
# 1 2 3 4 5
#
# Sample Output:
# 10 14

# Solution:

a,b,c,d,e = input().strip().split(' ')
array = [int(a),int(b),int(c),int(d),int(e)]

array.sort()

small_sum = sum(array[:4])
big_sum = sum(array[1:5])
print(str(small_sum) + " " + str(big_sum) )