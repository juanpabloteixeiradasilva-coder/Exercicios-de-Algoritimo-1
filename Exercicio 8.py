#Exercicio 8

soma = 0
while True:
    numero = float(input('Digite um numero (ou 0 para sair): '))
    if numero == 0:
        break
    soma = soma + numero

    print(f'A soma dos numeros digitados eh: {soma}')