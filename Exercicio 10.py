#Exercicio 10

primeiro = float(input('Digite o primeiro numero: '))
maior = primeiro
menor = primeiro

for i in range(2, 6):
    numero = float(input(f'Digite o {i}º numero: '))
    
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')