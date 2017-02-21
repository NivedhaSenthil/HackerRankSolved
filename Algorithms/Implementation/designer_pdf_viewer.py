# Sample Input
#
# 1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
# abc
# Sample Output
#
# 9
# Explanation
#
# We are highlighting the word abc:
#
# The tallest letter in abc is b, and height(b)=3. The selection area for this word is 3 * 1mm * 3mm = 9mm^2

# Solution:

h = list(map(int, input().strip().split(' ')))
characters = list(input().strip())

list_of_height_for_char = [h[ord(character) - 97] for character in characters]

max_height = max(list_of_height_for_char)

print(max_height * len(characters))