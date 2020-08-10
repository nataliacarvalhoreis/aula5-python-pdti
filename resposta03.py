# Faça um programa, com uma função que necessite de três argumentos, e
# que forneça a soma desses três argumentos.

def soma(a,b,c):
    soma = a + b + c
    return soma

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
c = int(input("Informe o terceiro número: "))

total = soma(a, b, c)
print("A soma dos números é: ", total)