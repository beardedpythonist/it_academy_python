#  if i.isascii():
counter = 0
counter2 = 0
line = str(input())
for i in line:
    if i.isascii() and i.isupper():
        counter2 = counter2 + 1
for i in line:
    if i.isascii() and i.islower():
        counter = counter + 1

print(counter)
print(counter2)

#
