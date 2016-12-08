# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o',
# and 'u'. For example, if s = 'azcbobobegghakl', your program should print:


s = 'azcbobobegghakl'  # example

count = 0

for c in s:
    if c is 'a' or c is 'e' or c is 'i' or c is 'o' or c is 'u':
        count += 1

print(count)