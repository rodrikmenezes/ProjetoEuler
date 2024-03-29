# =============================================================================
# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.
# =============================================================================


def fibonacci(n):
    ''' int -> int
    retorna o valor n da sequência de fibonacci
    OBS: n > 2
    '''
    a, b = 1, 2
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return c


def sequencia_fibonacci(x):
    ''' int -> int
    retorna um vetor com os números de fibonacci
    '''
    # os dois primeiros valores do vetor são dados
    vetor_fibonacci = [1, 2]
    for i in range(2, x):
        aux1 = vetor_fibonacci[len(vetor_fibonacci)-1]  # último valor do vetor
        aux2 = vetor_fibonacci[len(vetor_fibonacci)-2]  # penúltimo valor
        vetor_fibonacci.append(aux1 + aux2)
    return vetor_fibonacci


def soma_pares_fibonacci(x):
    ''' int -> int
    retorna a soma dos valores pares da sequência de fibonacci
    '''
    vetor_fibonacci = [1, 2]
    vetor_soma = []  # este vetor grava a soma dos valores pares até x
    soma = 2
    for i in range(2, x):
        aux1 = vetor_fibonacci[len(vetor_fibonacci)-1]  # último valor do vetor
        aux2 = vetor_fibonacci[len(vetor_fibonacci)-2]  # penúltimo valor
        vetor_fibonacci.append(aux1 + aux2)
        if vetor_fibonacci[i] % 2 == 0:
            soma += vetor_fibonacci[i]
            vetor_soma.append(soma)  # o vetor não é exibido no resultado
    return soma


# RESPOSTA 1 (minha resposta)
n = 3
while fibonacci(n) < 4000000:
    resposta = soma_pares_fibonacci(n)
    n += 1
print('Minha resposta: {}'.format(resposta))


# RESPOSTA 2 (Solução alternativa)
limite = 4000000
soma = 0
a = 1
b = 1
c = a + b
while c < limite:
    soma += c
    a = b + c
    b = c + a
    c = a + b
print('Resposta Alternativa: {}'.format(soma))
