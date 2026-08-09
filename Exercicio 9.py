#Exercicio 9

def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b


n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

resultado = maior_numero(n1, n2)
print(f"O maior número entre os dois é: {resultado}")