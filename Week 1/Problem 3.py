# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
# Longest substring in alphabetical order is: abc

s = 'abcbcd'  # example

string = ""
count = 0
longestCount = 0
longestString = ""
for i in range(len(s)):
    if i == 0:
        string += s[i]
        count += 1
    elif s[i] >= s[i - 1]:
        string += s[i]
        count += 1
    elif s[i] < s[i - 1]:
        if count > longestCount:
            longestCount = count
            longestString = string
        count = 1
        string = ""
        string += s[i]
    if i == len(s) - 1:
        if count > 1:
            if count > longestCount:
                longestCount = count
                longestString = string
print("Longest substring in alphabetical order is: " + longestString)
