# Faça um programa que use a função valorPagamento para determinar o valor a
# ser pago por uma prestação de uma conta. O programa deverá solicitar ao
# usuário o valor da prestação e o número de dias em atraso e passar estes valores
# para a função valorPagamento, que calculará o valor a ser pago e devolverá este
# valor ao programa que a chamou. O programa deverá então exibir o valor a ser
# pago na tela. Após a execução o programa deverá voltar a pedir outro valor de
# prestação e assim continuar até que seja informado um valor igual a zero para a
# prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório
# do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O
# cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem
# atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa,
# mais 0,1% de juros por dia de atraso.

def valorPagamento(prest, atraso):
    if atraso>0:
        prest = prest + (prest * 0.03) + (prest * 0.1*atraso)
    else:
        prest = prest
    return prest

soma = 0
quantidade = 0
valor_prest = float(input("Informe o valor da prestação: "))
while valor_prest != 0:
    dias = int(input("Informe a quantidade de dias em atraso: "))
    final = valorPagamento(valor_prest, dias)
    print("Valor final a ser pago: ", final)
    soma += final
    quantidade += 1
    valor_prest = float(input("Informe o valor da prestação: "))

print("Relatório do dia:")
print(" Quantidade de prestações : ", quantidade)
print("Valor total recebido: R$", soma)
