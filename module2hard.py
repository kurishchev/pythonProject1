b = int(input('Введите число из первой вставки:  '))


def parole(a):
    par_e = str()
    for i in range(1, a-1):
        for k in range(i+1, a-1):
            if a % (i+k) == 0:
                par_e = par_e + str(i)
                par_e = par_e + str(k)
    return par_e


ppp = parole(b)
print('Пароль: ', ppp)
