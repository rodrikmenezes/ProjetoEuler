# =============================================================================
# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
# =============================================================================

def quantidadeMultiplos(n):
    ''' Retorna o menor número divisível pela sequencia de 1 a n '''
    init = 2
    chute = 1000
    n_iter = 0
    while init <= n:
        n_iter += 1 
        num = chute / init
        if num % 2 != 0 and num % 2 != 1 :
            chute += 10
            init = 2
        else:
            init += 1
    return chute

# Resposta
print(quantidadeMultiplos(20))
