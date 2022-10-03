# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string
line = str(input())
string.punctuation
for p in string.punctuation:
    if p in line:
        line = line.replace(p, '')
 #   print(line)
x = line.split()
 #    print(x)
largest = len(x[0])
for i in range(1, len(x)):
     if len(x[i]) > largest:
         largest = len(x[i])
print(largest)
