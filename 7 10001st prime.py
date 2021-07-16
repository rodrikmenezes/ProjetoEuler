# =============================================================================
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prdme number?
# =============================================================================

# Ao executar o código abaixo, são impressos todos os números primos até 
# o valor inserido pelo usuário

def primo(x):
   """ Verifica se o número x é primo
   """
   n=0
   for i in range(1, x+1):
      if x % i == 0:
         n+=1
   if n < 3:
      return True
   else:
      return False

obj = int(input('Inserir um número inteiro = '))
i=0
n=2
while i < obj:
   if primo(n):
      i+=1
      print('{}° número primo = {}'.format(i, n))
   n+=1
