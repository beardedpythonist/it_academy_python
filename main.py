




n = int(input())
countertroyki = 0
poslzif = n % 10
count_poslzif = 0
count_chet = 0
count_bolsh5 = 0
poizbolsh7 = 1
count05 = 0
while n > 0:
        if n % 10 == 3:
             countertroyki =  countertroyki + 1
        if n % 10 == poslzif:
                count_poslzif = count_poslzif + 1
        if n % 2 == 0:
                count_chet = count_chet + 1
        if n % 10 > 5:
                count_bolsh5 = count_bolsh5 + (n % 10)

        if n % 10 > 7:
                poizbolsh7 = poizbolsh7 * (n % 10)
        if n % 10 == 0  or n % 10 == 5:
                count05 = count05 + 1

        n = n // 10

print(countertroyki, count_poslzif, count_chet, count_bolsh5, poizbolsh7, count05, sep='\n')



