# Faça um programa com uma função chamada somaImposto. A função
# possui dois parâmetros formais: taxaImposto, que é a quantia de imposto
# sobre vendas expressa em porcentagem e custo, que é o custo de um
# item antes do imposto. A função “altera” o valor de custo para incluir o
# imposto sobre vendas.

def somaImposto(taxaImposto, custo):
    custo = custo + custo * taxaImposto
    return custo

taxa = float(input("Informe a taxa de imposto: "))
custo = float(input("Informe o custo"))

final = somaImposto(taxa, custo)

print("O custo final é: ", final)