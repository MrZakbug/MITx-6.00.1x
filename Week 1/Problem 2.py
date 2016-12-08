# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob'
# occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

s = 'azcbobobegghakl'  # example

count = 0
i = 0


for c in s:
    if c is 'o' and i != 0 and i != len(s)-1 and s[i-1] is 'b' and s[i+1] is 'b':
        count += 1
    i += 1

print(count)