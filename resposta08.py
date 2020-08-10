# Faça uma função que informe a quantidade de dígitos de um
# determinado número inteiro informado.



def achaTamanho(x):
    return (len(str(x)))

num = int(input("Digite um número: "))
print(achaTamanho(num))

