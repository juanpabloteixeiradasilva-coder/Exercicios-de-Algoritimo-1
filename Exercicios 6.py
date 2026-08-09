#Exercicio 6

n = int(input('digite um numero inteiro: '))

soma = 0

for i in range(1, n + 1):
    soma += i

print(f'A soma dos {n} primeiros numeros inteiros eh: {soma}')