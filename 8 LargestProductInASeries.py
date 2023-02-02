"""
The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?
"""

# Importar módulo
import numpy as np

# Ler dados de um arquivo txt com 100 números
serie = open('serie1000numeros.txt', 'r')
num_str = list(serie.readline())

# Transformar str em número
num_int = []
for i in num_str:
    num_int.append(int(i))

def maiorProduto(lista, n):
    """ Retorna o maior produto de n números adjacentas da lista
    """
    i = n
    t = len(lista)
    r = 0
    while n <= t:
        lista_n = np.array(lista[n-i:n])
        p = np.product(lista_n)
        if p > r:
            r = p
            lista_s = list(lista_n)
        n += 1
    return lista_s, r

# Teste
# print(maiorProduto(num_int, 4))               # 9 × 9 × 8 × 9 = 5832

# Resposta
print(maiorProduto(num_int, 13))


