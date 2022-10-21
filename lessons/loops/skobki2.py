s = str(input())
ls = list(s)
count = 0
x = False
for c in range(len(ls)):
    if ls[0] == '(':
        if ls[c] == '(':
            count += 1
        if ls[c] == ')':
            count -= 1
            if count < 0:
                x = False
                break
        if count > 0:
            x = False
        else:
            x = True
print(x)


