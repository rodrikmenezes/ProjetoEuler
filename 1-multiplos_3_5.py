#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 21:15:14 2019

@author: rodrik
"""

# =============================================================================
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# =============================================================================


def soma_multiplos(x):
    ''' (int positivo) -> int
    soma dos multiplos de 3 e 5 menores que x
    '''
    vetor_multiplos = []
    n = 1
    while n < x:
        if n % 3 == 0 or n % 5 == 0:
            vetor_multiplos.append(n)
        n += 1
    return sum(vetor_multiplos)


# =============================================================================
# # Teste
# # soma_multiplos(10) -> 23
# print(soma_multiplos(10))
# =============================================================================

# RESPOSTA
print(soma_multiplos(1000))
