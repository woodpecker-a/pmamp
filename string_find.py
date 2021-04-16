#! usr/bin/python

s = str(input("Enter a sentence: "))
s = s.lower()
n = str(input("Which word you want to count: "))
print("'%s' comes %d time in this string!" %(n.upper(), s.count(n)))
