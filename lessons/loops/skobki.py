s = str(input())
ls = []
for c in range(len(s)):
    if s[c] == '(' or s[c] == '[' or s[c] == '{' or s[c] == ')' or s[c] == ']' or s[c] == '}':
        ls.append(s[c])    # перезапись в новый список только скобок
c = 0
while c <= len(ls):     # проверка на порядок следования 1
    if '(' in ls and ')' in ls:
        if ls[c - 1] == '(' and ls[c] == ')':
            del ls[ls.index('(')]
            del ls[ls.index(')')]
    if '[' in ls and ']' in ls:
        if ls[c - 1] == '[' and ls[c] == ']':
            del ls[ls.index('[')]
            del ls[ls.index(']')]
    if '{' in ls and '}' in ls:
        if ls[c - 1] == '{' and ls[c] == '}':
            del ls[ls.index('{')]
            del ls[ls.index('}')]
    c = c + 1
   # print(ls, 'после удалений парных скобок 1 попытка')
c = 0
while c <= len(ls):     # проверка на порядок следования 2
    if '(' in ls and ')' in ls:
        if ls[c - 1] == '(' and ls[c] == ')':
            del ls[ls.index('(')]
            del ls[ls.index(')')]
    if '[' in ls and ']' in ls:
        if ls[c - 1] == '[' and ls[c] == ']':
            del ls[ls.index('[')]
            del ls[ls.index(']')]
    if '{' in ls and '}' in ls:
        if ls[c - 1] == '{' and ls[c] == '}':
            del ls[ls.index('{')]
            del ls[ls.index('}')]
    c = c + 1
   # print(ls, 'после удаления пар 2 попытка')
c = 0
while c <= len(ls):     # проверка на порядок следования 3
    if '(' in ls and ')' in ls:
        if ls[c - 1] == '(' and ls[c] == ')':
            del ls[ls.index('(')]
            del ls[ls.index(')')]
    if '[' in ls and ']' in ls:
        if ls[c - 1] == '[' and ls[c] == ']':
            del ls[ls.index('[')]
            del ls[ls.index(']')]
    if '{' in ls and '}' in ls:
        if ls[c - 1] == '{' and ls[c] == '}':
            del ls[ls.index('{')]
            del ls[ls.index('}')]
    c = c + 1
 #  print(' после удаления пар 3 попытка')
if len(ls) == 0:
    print('скобки расставлены верно')
else:
    print('скобки расставлены неверно')