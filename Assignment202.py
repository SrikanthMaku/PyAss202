# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values


dict = {}

for value in range(ord('a'),ord('z')+1):
    dict[chr(value)] = value
     
print(dict)











