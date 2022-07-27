# Módulo Moeda - Dobro, metade, aumentando e diminuindo
# Dobro
def dobro(n):
    return n * 2


# Metade
def half(n):
    return n / 2


# Aumentando
def aumenta(n, x):
    r = n * x
    res = r / 100
    answer = n + res
    return answer


# Diminuindo
def diminui(n, y):
    r = n * y
    res = r / 100
    porcen = n - res
    return porcen
