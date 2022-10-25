
import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
symb = 'il1Lo0O'
n = int(input('введите количество паролей: '))
d = int(input('введите количество символов в пароле: '))
s1 = str(input('должен ли пароль содержать строчные буквы?  y - если да, n - если нет: '))
s2 = str(input('должен ли пароль содержать прописные буквы?  y - если да, n - если нет: '))
s3 = str(input('должен ли пароль содержать:  !#$%&*+-=?@^_,? y - если да, n - если нет:   '))
s4 = str(input('должен ли пароль цифры? y - если да, n - если нет:   '))
s5 = str(input('Исключать ли неоднозначные символы il1Lo0O?  y - если да, n - если нет: '))

def pass_generetion():
    char = ''
    alpha = ''
    alpha1 = ''
    if s1 == 'y':
        alpha = alpha + lowercase_letters
    if s2 == 'y':
        alpha = alpha + uppercase_letters
    if s3 == 'y':
            alpha = alpha + punctuation
    if s4 == 'y':
            alpha = alpha + digits
    if s5 == 'y':     # исключение
        alpha1 = ''
        for q in range(len(alpha)):
            if alpha[q] not in symb:
                alpha1 = alpha1 + alpha[q]
        alpha = alpha1

    for c in range(d):
        char = char + random.choice(alpha)
    print(char)


def quant_passes():
    for i in range(n):
        pass_generetion()


quant_passes()
