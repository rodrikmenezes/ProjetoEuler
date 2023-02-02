# =============================================================================
# The sum of the squares of the first ten natural numbers is 385
# The square of the sum of the first ten natural numbers is 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
# =============================================================================


def sumSquareDiff(x):
    ''' Diferença = Soma(n^2) - Soma(n)^2
    '''
    n = 0
    sn = 0  
    for i in range(1, x + 1):
        n += i
        sn += i*i

    return n**2 - sn


# Testes
print(sumSquareDiff(100))

