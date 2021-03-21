# =============================================================================
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# =============================================================================


import numpy as np

def palindromos():
    ''' Restorna uma lista de números palíndromos formados
    pela multiplicação entre outros dois números de dois dígitos'''
    
    palindromos = []
    
    for i in range(1, 1000):
        for j in range(1, 1000):
            p = i * j
            s = str(p)
            l = len(s)
            cont = 0
            n = int(np.floor(l/2))
            for w in range(0, n):
                ww = (w+1) * (-1)
                if s[w] == s[ww]:
                    cont += 1
            if cont == n:
                palindromos.append(p)
    return list(sorted(set(palindromos)))


# RESPOSTA
print(max(palindromos()))