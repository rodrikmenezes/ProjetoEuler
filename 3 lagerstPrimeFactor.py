# ==============================================================
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# ==============================================================


def fatoresPrimos(numero):
    ''' Retorna todos os fatores primos de um número dado '''
    n_fator = 2
    n_divisores = 0
    produtorio = 1
    fatores = []
    
    while n_fator < numero and produtorio != numero:
        if numero % n_fator == 0:
            n_divisores += 1
            fatores.append(n_fator)
            produtorio *= n_fator
        n_fator += 1

    return fatores


# Resposta final do problema
print(max(fatoresPrimos(600851475143)))






